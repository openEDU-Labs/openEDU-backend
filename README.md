# openEDU-backend

This is the backend application for the website. 

This tutorial is pretty great for learning Django in general
https://docs.djangoproject.com/en/1.8/intro/tutorial01/

This one is pretty great for learning Heroku 
https://devcenter.heroku.com/articles/getting-started-with-django

The general procedure to get things running is:

1. Install Heroku toolbelt

2. Clone this repository into some directory

3. Make your changes and push back, it will automatically be deployed, don't screw anything up because that makes actual changes!!

To run locally, you need to:

1. be running in a virtual env
"virtualenv venv"
"source venv/bin/activate"

2. call "heroku pg:pull open-edu::database drkhcv6ebttof"

3. call "python manage.py migrate"

3. call "python manage.py runserver"

4. view whatever changes you made

