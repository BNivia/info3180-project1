release : python manage.py db upgrade --info3180-project1 migrations
web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app
