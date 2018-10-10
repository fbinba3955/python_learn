import pymysql
pymysql.install_as_MySQLdb()


# PostgreSQL配置
DATABASES = {
    'default': {
        'NAME': 'sjt',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'root',
        'PASSWORD': 'sjt3953395'
    }