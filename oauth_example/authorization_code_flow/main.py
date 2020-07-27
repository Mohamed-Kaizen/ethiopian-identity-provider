from typing import List

import uvicorn
import httpx
from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from models import User_Pydantic, User
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

server_url = "http://127.0.0.1:8000/"

client_id = "deHqCJTauxHBZsqrfSqZvKuwxz91D42vFbU7Lryh"

client = httpx.AsyncClient()


@app.get("/login/")
def login_via_eia(request: Request):
    state = "random_state_string"
    response_type = "code"
    scope = "user"
    redirect_uri = f'{server_url}/o/authorize/?scope={scope}&state={state}&response_type={response_type}&client_id={client_id}'
    return RedirectResponse(redirect_uri)


@app.get("/callback/")
async def auth_via_eia(request: Request):
    code = request.query_params.get("code")

    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": "3QRyap6kS6U1BcPiAPzln0deK0x9iVpXCaOvnTe7P7zgYJQ8al1lXg2GpXlAOVkmK4Daz4iRf5WdODYDhCvtF4EGZqKueSrk6OZaKXuQVsVjK0p3xEeYsjrakLzdHpcU",
    }

    response = await client.post(f"{server_url}/o/token/", data=payload)

    data = response.json()

    headers = {"Authorization": f"Bearer {data.get('access_token')}"}

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
        reload=True,
        log_level="debug",
    )
