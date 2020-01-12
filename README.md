# REACT JS #
In the project directory(cd reactjs) and run below command:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### `npm test`

### `npm run build`

### `npm run eject`



# PYTHON #

### DATABASE:

- Create Database in POSTGRESQL, fallow the below command:
```
CREATE USER <user_name> WITH PASSWORD;
CREATE DATABASE <db_name> WITH OWNER <user_name>;
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <user_name>;
```

In the project directory(cd python) and run below command:
- Create `local.py` from `cashcog_coding_challenge/settings` and add the below code:

```
import os

DEBUG = True
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME', 'cashcog'),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'USER': os.environ.get('DB_USER', 'cashcog'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'cashlog'),
            'PORT': os.environ.get('DB_PORT', '5432')
    }
}

CASHCOG_EXPENSE_API_URL = os.environ.get('CASHCOG_EXPENSE_API_URL', 'https://cashcog.xcnt.io/single')

```

### apply migration and run project:
```
./manage.py migrate
./manage.py runserver
```

### Create JWT Token
```
login in admin site and create user and token after that copy the token and add in reactjs api call
```

### API Detail for Insert/Update/ data:
url_end_point: `http://localhost:8000/expense/` with POST call to Insert/update data and to get data with GET call same end_point

### API Detail for filtering:
url_end_point: `http://localhost:8000/filter/expense/` with GET call
params: `query`

