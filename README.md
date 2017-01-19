====
RAD City Website
====

## Prerequisites
- Python 3


##Setup

1. Create a virtual environment with `pyvenv env` (unless you're installing it outside the folder, please name the environment folder "env")
2. `pip install -r requirements`
3. Create a new settings file in `pdxrad/settings/`, you can copy the `template.py` file* 
4.
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

*If you're running locally, name it `local.py`, otherwise you'll need to create an `environment.py` file in root and change the `DJANGO_SETTINGS_MODULE` variable