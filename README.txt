This is a Mezzanine project: http://mezzanine.jupo.org/

You can browse the code of the relevant version of Mezzanine at:
https://github.com/stephenmcd/mezzanine/tree/1.3.0

Here's how to set up your own local instance of this project:
(I should probably update these instructions to use a virtualenv at some point...)

sudo apt-get install python-pip
sudo pip install mezzanine
sudo pip install mezzanine-events
git pull git://github.com/chrisboyle/lashsite.git
cd lashsite
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
        "USER": "", "PASSWORD": "", "HOST": "", "PORT": "",
    }
}
EOF
python manage.py createdb
python manage.py runserver


Now visit http://localhost:8000/admin
* Create a "Rich-text page" called "Home" with URL "/"
  * un-tick show in navigation (it's already shown automatically)
  * don't include the gig/blog panels; they're in templates/pages/index.html
* Create an "Event container" called "Gigs" with URL "/gigs"
