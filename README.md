docker start djngo
eval $(docker-machine env django)
docker run -P --name pg_test eg_postgresql
docker container ls
# modify mysite/settings.py
python3 manage.py runserver 8080
python3 manage.py createsuperuser
python3 manage.py makemigrations polls
python3 manage.py migrate
