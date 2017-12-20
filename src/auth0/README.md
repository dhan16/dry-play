# Auth0 Angular Frontend and Django REST API Backend

This sample demonstrates how to add authentication to an Angular SPA which uses a Django REST API as a backend.

# Getting Started

## Set the Client ID and Domain

1. [sign up](https://auth0.com) for your Auth0 account and create a new client in the [dashboard](https://manage.auth0.com). Find the **domain** and **client ID** from the settings area and add the URL for your application to the **Allowed Callback URLs** box. (eg `http://localhost:4200`).
Add the **client ID** and **domain** to frontend_angular2/src/app/auth/auth0-variables.ts.

2. cd frontend_angular && npm install

## Run the Application

npm start
