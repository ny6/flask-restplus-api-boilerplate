## Flask Rest API


### Env Vars

* FLASK_ENV = "production | test | development" [Default development]
* SECRET_KEY = "secret_key"
* POSTGRES_URL = "127.0.0.1:5432"
* POSTGRES_USER = "user_name"
* POSTGRES_PW = "password"
* POSTGRES_DB = "db_name"
* POSTGRES_TEST_DB = "test_db_name"


### Run Migrations

```bash
python manage.py db init
python manage.py db migrate --message 'initial database migration'
python manage.py db upgrade
```
