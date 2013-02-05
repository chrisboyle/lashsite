This is a Mezzanine project: http://mezzanine.jupo.org/

Local working environment setup:

sudo apt-get install python-pip
sudo pip install mezzanine
sudo pip install mezzanine-event
python -c 'import random; print "SECRET_KEY = \"%s\"" % ("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))' >local_settings.py
cat <<EOF >>local_settings.py

DEBUG = True

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
EOF
python manage.py createdb
