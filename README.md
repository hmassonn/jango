docker-machine start django
eval $(docker-machine env django)

docker run --rm -P --name pg_test eg_postgresql
# if problem :
# docker build -t eg_postgresql .

# for psql connection:
# docker run --rm -t -i --link pg_test:pg eg_postgresql bash
# docker run -it eg_postgresql bash
# psql -h localhost -p 32768 -d docker -U docker --password

docker container ls
# modify mysite/settings.py
python3 manage.py runserver 8080
python3 manage.py makemigrations polls
python3 manage.py migrate
python3 manage.py createsuperuser
