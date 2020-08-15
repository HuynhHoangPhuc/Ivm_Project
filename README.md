# Ivm_Project

## Install pipenv

For Windows and Macos:`pip install pipenv`
For Linux(Ubuntu): `pip3 install pipenv`

## Install package and active environment

     pipenv install
     pipenv shell
  
## Update database
  
     python manage.py db init
     python manage.py db migrate --message 'initial database migration'
     python manage.py db upgrade

## Run database

    docker stop $(docker ps -a -q) && docker-compose up
    
## Start server

    python manage.py run
    
## Testing

    python manage.py test
