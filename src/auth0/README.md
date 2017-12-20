# Auth0 Angular Frontend and Django REST Framework API Backend

This sample demonstrates how to add authentication to an Angular SPA which uses a Django REST API as a backend.
Please check [Quickstart](https://auth0.com/docs/quickstart/backend/django) to better understand this sample.


## Getting Started

1. [sign up](https://auth0.com) for your Auth0 account and create a new client in the [dashboard](https://manage.auth0.com). Find the **domain** and **client ID** from the settings area and add the URL for your application to the **Allowed Callback URLs** box. (eg `http://localhost:4200`).

2. Authorization
    * Setup the Authorization extension. Ref: https://auth0.com/docs/extensions/authorization-extension/v2#how-to-install
    * This is crucial: DO NOT ADD ANY SCOPES to the backend API. Instead add permissions to the Authorization extension and, after publishing the authorization rule, add the rule in access_token_scopes_rule.txt which adds the permissions to the returned scopes. The backend API works off these scopes.


## Frontend

### Setup

1. Add the **client ID** and **domain** to frontend_angular2/src/app/auth/auth0-variables.ts.
2. cd frontend_angular && npm install

### Run

npm start


## Backend

### Setup

1. change backend_django/.env
AUTH0_DOMAIN=example.auth0.com
API_IDENTIFIER=YOUR_API_AUDIENCE
2. python3 -m venv ~/work/python-virtualenvs/dry-play-auth0
3. source ~/work/python-virtualenvs/dry-play-auth0/bin/activate
4. pip3 install -r ~/work/dry/dry-play/src/auth0/backend/django/requirements.txt

### Run

1. source ~/work/python-virtualenvs/dry-play-auth0/bin/activate
2. python manage.py migrate
3. python manage.py runserver 0.0.0.0:3010
