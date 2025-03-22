# Contact Hub 

## Overview 

A simple contact hub for managing contacts. This is a learning project to practice Django and HTMX.

## Development 

1. Create a virtual environment

I use uv to manage the virtual environment. And I strongly recommend you to use uv as well. I fast, reliable and easy to use.

```bash 
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

2. Migrate the database

```bash 
python manage.py migrate

# When you make changes to the models, you need to migrate the database again
python manage.py makemigrations
python manage.py migrate
```

3. Run the development server

```bash 
python manage.py runserver
```

Open the browser and navigate to `http://localhost:8000`

4. After confirming the server is running, you can create a superuser to access the admin panel.

```bash 
python manage.py createsuperuser
```

Navigate to `http://127.0.0.1:8000/admin/login/?next=/admin/` to access the admin panel.

