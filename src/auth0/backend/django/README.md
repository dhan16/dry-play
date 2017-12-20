# Auth0 + Python + Django REST Framework API Seed

Please check our [Quickstart](https://auth0.com/docs/quickstart/backend/django) to better understand this sample.

# Running the example

```bash
# .env file
AUTH0_DOMAIN=example.auth0.com
API_IDENTIFIER=YOUR_API_AUDIENCE

```

1. python3 -m venv ~/work/python-virtualenvs/dry-play-auth0
2. source ~/work/python-virtualenvs/dry-play-auth0/bin/activate
3. pip3 install -r ~/work/dry/dry-play/src/auth0/backend/django/requirements.txt
4. python manage.py migrate
5. python manage.py runserver 0.0.0.0:3010

# Testing the API

Try the following APIs from the SPA:

1. GET [http://localhost:3010/api/public](http://localhost:3010/api/public)
2. GET [http://localhost:3010/api/private](http://localhost:3010/api/private) which will
throw an error if you don't send an access token signed with RS256 with the appropriate issuer and audience in the
Authorization header. 
3. GET [http://localhost:3010/api/private-scoped/](http://localhost:3010/api/private-scoped) which will throw an error if
you don't send an access token with the scope `read:messages` signed with RS256 with the appropriate issuer and audience
in the Authorization header.
