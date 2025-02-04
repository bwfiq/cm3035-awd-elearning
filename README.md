# Project Setup
- Initialise a venv
- run the following commands
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

ALLOWED_HOSTS in `settings.py` is set to allow all connections for debug purposes.

The superuser for logging into the django admin panel is admin:admin.

# TODO

- [ ] Initialise a Django application
- [ ] Dockerise it
- [ ] Implement github actions for testing and building
- [ ] Deploymentation
- Rest of the horse
