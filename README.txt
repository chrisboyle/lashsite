This is a Mezzanine project: http://mezzanine.jupo.org/

Here's how to set up your own local instance of this project:
(I should probably update these instructions to use a virtualenv at some point...)

git pull git://github.com/chrisboyle/lashsite.git
cd lashsite
sudo apt-get install python-pip
sudo pip install -r requirements/project.txt
python mk_local_settings.py
python manage.py createdb
python manage.py runserver


Now visit http://localhost:8000/admin
* Create a "Rich-text page" called "Home" with URL "/"
  * don't include the gig/blog panels; they're in templates/pages/index.html
* Create an "Event container" called "Gigs" with URL "gigs"
