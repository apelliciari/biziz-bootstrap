# clone con github windows

# creiamo il virtual env

C:\Home\web\github\biziz-bootstrap>mkdir .venv
C:\Home\web\github\biziz-bootstrap>cd .venv
C:\Home\web\github\biziz-bootstrap\.venv>virtualenv --no-site-packages .
New python executable in .\Scripts\python.exe
Installing setuptools................done.
Installing pip...................done.

# attiviamo il virtual env! lo vediamo dalle parentesi prima del percorso shell
C:\Home\web\github\biziz-bootstrap\.venv>.\Scripts\activate.bat

# installiamo django, le extensions e south
(.venv) C:\Home\web\github\biziz-bootstrap\.venv>pip install django
(.venv) C:\Home\web\github\biziz-bootstrap\.venv>pip install django-extensions
(.venv) C:\Home\web\github\biziz-bootstrap\.venv>pip install South

# creiamo il progetto django
(.venv) C:\Home\web\github\biziz-bootstrap>django-admin.py startproject biziz_bootstrap

# creiamo la app django
C:\Home\web\github\biziz-bootstrap>python biziz_bootstrap\manage.py startapp frontend

## aggiorniamo il db con syncdb
(.venv) C:\Home\web\github\biziz-bootstrap>python biziz_bootstrap\manage.py syncdb
Creating tables ...
Creating table auth_permission
Creating table auth_group_permissions
Creating table auth_group
Creating table auth_user_groups
Creating table auth_user_user_permissions
Creating table auth_user
Creating table django_content_type
Creating table django_session
Creating table django_site

You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (leave blank to use 'alessandro'): admin
Email address: admin@adadmin.it
Password:
Password (again):
Superuser created successfully.
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)

# vediamo tutti i comandi disponibili di manage.py ( dipendono dalle app installate nei settings.py del progetto)
(.venv) C:\Home\web\github\biziz-bootstrap>python biziz_bootstrap\manage.py help

# iniziamo a gestire le migrazioni con south http://south.readthedocs.org/en/latest/index.html
(.venv) C:\Home\web\github\biziz-bootstrap>python biziz_bootstrap\manage.py schemamigration frontend --initial
Creating migrations directory at 'C:\Home\web\github\biziz-bootstrap\frontend\migrations'...
Creating __init__.py in 'C:\Home\web\github\biziz-bootstrap\frontend\migrations'...
 + Added model frontend.Azienda
 + Added M2M table for tags on frontend.Azienda
 + Added model frontend.Prodotto
 + Added model frontend.Tag
Created 0001_initial.py. You can now apply this migration with: ./manage.py migrate frontend

# le applichiamo
(.venv) C:\Home\web\github\biziz-bootstrap\biziz_bootstrap>python manage.py migrate frontend
Running migrations for frontend:
 - Migrating forwards to 0001_initial.
 > frontend:0001_initial
 - Loading initial data for frontend.
Installed 0 object(s) from 0 fixture(s)


# dopo aver fatto una modifica ai modelli, creiamo una nuova migrazione e poi la applichiamo
(.venv) C:\Home\web\github\biziz-bootstrap\biziz_bootstrap>python manage.py schemamigration frontend --auto
 + Added field indirizzo on frontend.Azienda
Created 0002_auto__add_field_azienda_indirizzo.py. You can now apply this migration with: ./manage.py migrate frontend

(.venv) C:\Home\web\github\biziz-bootstrap\biziz_bootstrap>python manage.py migrate frontend
Running migrations for frontend:
 - Migrating forwards to 0002_auto__add_field_azienda_indirizzo.
 > frontend:0002_auto__add_field_azienda_indirizzo
 - Loading initial data for frontend.
Installed 0 object(s) from 0 fixture(s)

# usiamo shell_plus dalle django extensions per giocare con i modelli

(.venv) C:\Home\web\github\biziz-bootstrap\biziz_bootstrap>python manage.py shell_plus
