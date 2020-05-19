# Grocecy Data Pipeline

## Setup Gmail Access

In order to send and retrieve the receipt pictures, a Gmail account was created. Gmail was choosen because it can generate additional passwords for an application, such as this one, to have access to email.

### Create the Gmail Account

First step is to create the email account that pictures will be sent to. Go to https://accounts.google.com/SignUp to create the email account, following the steps.

### Turn on 2 Factor Authentication

Since the generated passwords that will be used in the python script are less secure and give whoever has them full access to the account, 2 factor authentication is required to create them.

Go to https://support.google.com/accounts/answer/185839 for instructions on how to activate 2 factor authentication.

> If you account is managed by an organization, such as a school email, you may not be able to create genearted passwords.

### Create an App Password

Back on https://accounts.google.com/SignUp, you should now see an option in the  **Signing in to Google** section that says **App passwords**. Click this to create a new app password. Since creating an app password will give access to your Google account, you will be prompted to sign in again.

Create the name of the app that you will be connecting to your Gmail with. The app and device are inconsequential. For example, I created an app named **Email - python**. Clicking on **Generate** will give give you the password for that app.

> **CAUTION:** This password grants full permission to your entire Google Account. Keep it safe!

## Python Email Access

Next, let's construct a simple python script that can read all the emails in our newly created account.
