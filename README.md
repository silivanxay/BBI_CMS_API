# Bamboo BI  Content Management System Headless API

This application enables Django powered websites to have multiple tenants via PostgreSQL schemas. A vital feature for every Software-as-a-Service website.
        
    # Creat a new database
    CREATE DATABASE 'bbi_ecomm'


### Basic Settings for Development
Activate environment

    python  -m venv  venv
    source venv/bin/activate

Install dependencies

    pip install -r requirements.txt


Basic Settings
You’ll have to make the following modifications to your your .env file
and Django Secret Key


    DB_NAME=your_database_name
    DB_USR=your_user_name
    DB_PWD=your_password

    SECRET_KEY='your_secret_key'

or to your bbi_ecomm/settings.py file

Your DATABASE_ENGINE setting needs to be changed to

    DATABASES = {
    'default': {
            # Tenant Engine
            'ENGINE': 'django_tenants.postgresql_backend',
            # set database name
            'NAME': 'your_db_name',
            # set your user details
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'POST': '5432'
        }
    }

Make migrations and Apply to database

    # create migrations files (every new django app)
    python manage.py makemigrations
    python manage.py makemigrations tenant
    python manage.py makemigrations bbi_exchange
    python manage.py makemigrations product
    # Apply migrations
    python manage.py migrate
    python manage.py migrate easy_thumbnails

To set up Lao language, it is required gettext library:

For Ubuntu:

    sudo apt install -y gettext

For Mac:

    Brew install gettext

then, make folder in project directory:


    python manage.py makemessages -l la -i venv
    python manage.py compilemessages -l la
    python manage.py migrate

Setup Initial User, Tenant and Admin
        
    # create first user
    python manage.py createsuperuser
    # Create the Public Schema
    python manage.py create_tenant
        # example
        schema name: public
        user: 1
        paid until:2022-12-31
        on trial:False
        is active: True
        domain:localhost
        
    # Create the Administrator
    python manage.py create_tenant_superuser
        # example
        Enter Tenant Schema ('?' to list schemas):  public
    python manage.py runserver

For Checking before deploy
    
    # API/ Unit Test
    python manage.py test
        
    # Deploy checklist
    python manage.py check --deploy

    # Check Style
    pip install flake8
    flake8 martor_demo/ --max-line-length=127

### Basic setting for deployment
To run by using Docker 
    
    # Build Docker images
    docker build . --network=host

    #R Run Docker container
    docker run -p 8000:8000 #image_id --network=host