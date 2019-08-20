python3 manage.py createsuperuser
python3 manage.py makemigrations polls
python3 manage.py migrate
docker run -P --name pg_test eg_postgresql
