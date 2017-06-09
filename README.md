# Eventex

Event system ordered by Morena.

## Development

1. Clone this repo.
2. Create a virtualenv with python 3.6.
3. Activate the virtualenv created on step before.
4. Install the dependencies.
5. Configure your dev instance with a .env file
6. Run tests.

```console
git clone git@github.com:joaopcanario/eventex.git eventex
cd eventex
python -m venv .eventex
source .eventex/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Deploy

1. Create an app on Heroku.
2. Send configurations to Heroku.
3. Set a safe SECRET_KEY to your app.
4. Set DEBUG=False.
5. Configure the mail service.
6. Send the code to Heroku.

```console
heroku create myapp
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure email (e.g.: sendgrid)
git push heroku master --force
```
