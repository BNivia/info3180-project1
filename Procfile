release : python3 manage.py db upgrade --app migrations
web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app
