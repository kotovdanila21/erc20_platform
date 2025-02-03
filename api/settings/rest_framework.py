from api import settings

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'app.base.renderers.ORJSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'app.base.parsers.ORJSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'app.base.authentications.session.SessionAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    "DEFAULT_THROTTLE_RATES": {
        "anon": settings.env("ANON_THROTTLE_RATE", default="20000/s"),
        "user": settings.env("USER_THROTTLE_RATE", default="50000/s"),
    },
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"
}