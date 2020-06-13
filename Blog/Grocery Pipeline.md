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

## Setup AWS S3 Instance

In case there are ever any refinements made to the image processing or the database holding all the processed data fails, we will need to store the image files somewhere safe. AWS offers S3, a cheap cloud storage solution that will hold all of our files.

## Python Access to AWS S3

To send the image files from the computer processing them to the AWS S3 cloud storage, we will write a python script.

## Python Processing the images using Tesseract OCR

To pre-process and read the text from the images, we will be using Tesseract OCR.

## Python Processing of Raw Text

Once the text has been read out of the image files, it will need to be parsed to be usable later on.

## Setting up Raspberry Pi

To help simulate a more realistic environment, the database that holds the data will be created on a remote machine, in this case a Raspberry Pi. This requires some basic networking and Linux skills.

## Setting up MySQL on Raspberry Pi

The process of creating the database on a Raspberry Pi is identical to setting it up on any other Linux box.

## Creating The Data Model

The data model for the project will keep things simple and make sure to follow some basic design principles. Loading it to the MySQL instance will also be a breeze with the design tool.

## Using Python to load the Database with processed data

Python will be used to send the data to the database.

## Some Fun With SQL Queries

After the data has been loaded to the database, we want to ensure that all table joins work as expected and that we are able to write queries that accomplish all of the main tasks we want to perform later.

## Building the Tableau

Tableau is a leader in the BI and dashboarding spaces. Here is how we are going to display the data for viewing.

## Building the Basket Analysis Model in R

To find out what people are likely to buy if they buy certain items, we will build an apriori model in R.

## Embedding an R Model in Tableau

To use the model, we will need a presentation layer.

## Creating an API for the R model

When deploying models in a production environment, API's are a system agnostic way to allow access.

## Creating a Shiny Application

Another way to present data, Shiny applications are more user friendly for people to use.
