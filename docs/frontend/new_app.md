# Ingrate you system with ETP


In this tutorial we will show you how to `Ingrate you system with ETP`.
you need to complete [How to load dump data tutorial](/backend/load_dump_data/)

If you currently signed just click the sign out icon. Then enter the following account:

    username: mila
    password: 1234567899mnm

on the right side of the dashboard you will see button `Create Your App` clicked. It will open new tab
you will notice the domain has been changed, now it will ask you to sign in if you didn't do that before.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/frontend/profile_app.png)

once you sign in you will see empty list of app, click on `New App`

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/frontend/profile_app_list.png)

you will see a form with the follow:

    - `Name`: The app name.
    - `Client type`: what kind of security will you use .
    - `Authorization grant type`: Which oauth protocol will you choose.
    - `Redirect uris`: Once the process of authorization is finished where to redirect the user.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/frontend/profile_app_form.png)

once you click save you it will take you to `App` detail page. You will notice two new fields `client id` and `client secret` you need this two keys in you app.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/frontend/profile_app_detail.png)


 Then you need to follow the [Oauth follow](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2)

