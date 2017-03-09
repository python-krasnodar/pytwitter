# PyTwitter
This is a project for my portfolio. I created it for fun. This is something like a microblogging system like Twitter.

## Up and Running
First, install the packages:
```
pip install -r requirements.txt
```
**Note.** _Optionally, you can use virtualenv._

Next, you need to configure the local settings. For this you need to create a file `local_setting.py`. Here is an example of a file to override a database connection.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pytwitter',
        'USER': 'pytwitter',
        'PASSWORD': 'pytwitter',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```

Now we can apply the database migration with this simple command
```
./manage.py migrate
```

Finally, start the local web server for development.
```
./manage.py runserver
```

