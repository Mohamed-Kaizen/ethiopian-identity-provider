from typing import List

import uvicorn
import httpx
from fastapi import FastAPI, Request, HTTPException, status
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from models import User_Pydantic, User, StateCode
from utils import unique_state_code
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI(title="FastAPI Authorization code flow example")

app.add_middleware(SessionMiddleware, secret_key="some-random-string")

register_tortoise(
    app,
    db_url="sqlite://./fastAPI_db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

server_url = "https://ethiopia-identity-provider.herokuapp.com"

client_id = "deHqCJTauxHBZsqrfSqZvKuwxz91D42vFbU7Lryh"

client = httpx.AsyncClient()


@app.get("/login/")
async def login_via_eia(request: Request):
    state = await StateCode.create(code=unique_state_code(), is_used=False)

    response_type = "code"

    scope = "user"

    redirect_uri = f'{server_url}/o/authorize/?scope={scope}&state={state.code}&response_type={response_type}&client_id={client_id}'

    return RedirectResponse(redirect_uri)


@app.get("/callback/")
async def auth_via_eia(request: Request):
    # Getting the code, state and error (if there is any error) from the request
    code = request.query_params.get("code")

    callback_state = request.query_params.get("state")

    error = request.query_params.get("error")

    if error:
        # Raise error if user deny the access.

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"detail": "You can't use our app b/c you deny the access :("}
            )

    state = await StateCode.get_or_none(code=callback_state, is_used=False)

    if not state:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"detail": "You can't use this :("})

    state.is_used = True

    await state.save()

    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": "3QRyap6kS6U1BcPiAPzln0deK0x9iVpXCaOvnTe7P7zgYJQ8al1lXg2GpXlAOVkmK4Daz4iRf5WdODYDhCvtF4EGZqKueSrk6OZaKXuQVsVjK0p3xEeYsjrakLzdHpcU",
    }

    # Exchange code with access token
    response = await client.post(f"{server_url}/o/token/", data=payload)

    data = response.json()

    headers = {"Authorization": f"Bearer {data.get('access_token')}"}

    # Getting user info using access token
    user_info_response = await client.get(f"{server_url}/api/users/o/userinfo/", headers=headers)

    user_info = user_info_response.json()

    user = await User.get_or_none(uuid=user_info.get("uuid"))

    if not user:
        uuid = user_info.get("uuid")
        username = user_info.get("username")
        email = user_info.get("email")
        picture = user_info.get("picture")
        user = await User.create(uuid=uuid, username=username, email=email, picture=picture)

    return await User_Pydantic.from_tortoise_orm(user)


@app.get("/users/", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=5000,
        log_level="debug",
    )
