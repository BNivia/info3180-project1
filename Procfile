release : python manage.py db upgrade --info-project1 migrations
web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app
