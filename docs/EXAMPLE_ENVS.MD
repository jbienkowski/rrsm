# /git/rrsm/src/rrsm/.env
    SECRET_KEY='#ps1ib&=v%zsgzi5q*qp-ei*b1bg19dxv&861m@4@x+2ww6nx^'
    DEBUG=True
    ALLOWED_HOSTS=.localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3
    DATABASE_ENGINE = "django.db.backends.sqlite3"
    DATABASE_NAME = ".rrsm.db"
    DATABASE_USER='admin'
    DATABASE_PASS='passwd'
    EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
    CACHE_BACKEND=django.core.cache.backends.memcached.MemcachedCache
    CACHE_LOCATION='127.0.0.1:11211'
    CACHE_TIME_SHORT=60
    CACHE_TIME_MEDIUM=300
    CACHE_TIME_LONG=1800
    RRSM_URL_BASE='rrsm2/'

# Cache backends
* `django.core.cache.backends.dummy.DummyCache` (development)
* `django.core.cache.backends.memcached.MemcachedCache`
* `django.core.cache.backends.filebased.FileBasedCache`