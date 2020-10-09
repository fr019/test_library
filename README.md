test_library

Start application server:

    $ docker-compose up -d

Apply migrations:

    $ docker-compose run --rm django python manage.py migrate

Populate database:
     
    $ docker-compose run --rm django python manage.py loaddata db.json

Credentials:

    username: admin
    password: admin
    
    username: test1
    password: 4rfv4rfv

[Login page](http://localhost:8000/accounts/login/)
[Author endpoint](http://localhost:8000/api/authors/)
[Books endpoint](http://localhost:8000/api/books/)
[Subscriber endpoint](http://localhost:8000/api/subscribers/)
