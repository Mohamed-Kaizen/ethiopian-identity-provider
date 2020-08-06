# Renew And Businesses

In this tutorial we will show you how staff accepted renew request and accepted/deny business request.
you need to complete [How to load dump data tutorial](/backend/load_dump_data/)

##  Renew
First login as `mohamed` with password `1234567899mnm`. Now you are login as staff user, from the dashboard 
you see link called `Renews` clicked and you will see list of renew request.

![Screenshot](/img/renew_list.png)

Click the action drop down menu and select `Mark selected request as Accepted` and select `bugs bunny` request
and click go button.

![Screenshot](/img/renew_list2.png)

And you notice that `bugs bunny` request has been accepted, go to `bugs bunny` profile see the `expire_at`,
the date it been updated by renew request created_at + 1 year.


##  Businesses
First login as `mohamed` with password `1234567899mnm`. Now you are login as staff user, from the dashboard 
you see link called `Businesses` clicked and you will see list of businesses request.

![Screenshot](/img/businesses_list.png)

Click the action drop down menu and select either `Mark selected business request as Accepted` 
or `Mark selected business request as Deny` and select `Strategy Tap` request
and click go button.And you notice that `Strategy Tap` request has change the is active state.


