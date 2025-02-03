from api.settings import env

GUNICORN_WORKERS = env.int("GUNICORN_WORKERS", default=4)

loglevel = "debug"
bind = "0.0.0.0:9090"
workers = GUNICORN_WORKERS
reload = True