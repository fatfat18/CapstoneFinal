//web: gunicorn --bind 0.0.0.0:$PORT SafeSight:app
web: gunicorn SafeSight.wsgi:application
python manage.py collectstatic --noinput
manage.py migrate
