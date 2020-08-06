# Command

## Groups

We will start by creating **`Group`** that will help us to set permission for our users and keep our
 process of setting up permission **`DRY`**.

Go to `/admin/` and fellow the setup

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/admin_login_page.png)

You see a form , enter your **username** and **password**

??? attention
    In case you can't login. Please see [How to setup the database and create superuser account](/backend/command).

After successfully login to the admin page you will see the dashboard.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/dashBoard.png)

click on **Groups** link.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/group_list.png)

you will see empty list with only search bar. click **ADD GROUP**

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/create_group.png)

create new group with the following permission. And click save, once you did that you see new group called `python`
in group list view.


## Staff

Now if you created group it time to assign the group to the staff user. Go back to the Dashboard and scroll down
and you will see link called `Profiles` clicked.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/dashboard_profile.png)

Once you click the link you will see `one profile` and that is your current account. Now create new account
by clicking on `ADD Profile`.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_list.png)

Once you do that you will see form with different section we will see every section in separate

- The first section will see is the username section

   ![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_create_username.png)

- The next section will be is `the Personal info section`

   ![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_create_personal_info.png)

- The next section will be is `the Permissions section`

   ![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_create_permissions.png)

??? danger
    - **Staff checkbox:** this checkbox will only give users to login to the admin page. To restrict there permission
    in the admin we should add them to the group `python`, see [How to setup A Group](/backend/group_and_staff/#groups).
    - **Superuser Check:** this checkbox is different from `staff checkbox` in way that will give a user full permissions
     in the admin page the same permissions as you current user.

- The next section will be is `the ADDRESSES and FINGERPRINTS section`

   ![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_create_other.png)


Once you save you will see new profile has been added in the profile list view

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_list2.png)


## Bonus

This is Bonus round you don't need to do it if you don't want too.

## Exporting users to .....

We will show you how to export the data from the database into `(csv|xls|xlsx|tsv|ods|json|yaml|html)`.
It easy just follow the image

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_list3.png)

That it :), now downloading will start.

## Revision
In this section we will show you how to do `revision`. **What is Revision ?**
will it like a history for a certain record or object.
Go to one of the created user profile by clicking there username

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_detail.png)

now let change there username, once you done that click `save and continue editing` at bottom. 
Then after the page refreshed you will see `History` button at the top right just clicked.
You will see list of history with `compare` button at the top.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_history.png)

As you can see the top selected one is the latest record about the object.
And the one blow is the old record of the object. Let compare them my clicking `compare`

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_history_compare.png)

You will see two color red and green. The red indicate the remove/edit field or the old record,
the green indicate added/edited field. Now let say we want to go back to the old record. Just click 
`Revert to this version`, it will took you to the user detail page, you many say "This is the same" but is not see
the username field it go back to the old version, now click `save` to go back to this record.
Once you done that you will redirected to the profile list view now go that use and see his history.

![Screenshot](https://raw.githubusercontent.com/Mohamed-Kaizen/ethiopian-identity-provider/master/docs/img/profile_history2.png)

you will notice new record has been add `Reverted to previous version,`, this show you the revision will even record
the revision process.
