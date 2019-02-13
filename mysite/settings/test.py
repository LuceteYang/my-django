from mysite.settings.base import *
# local 환경이니까 디버그 모드를 켜야지!
DEBUG = true

# local 데이터베이스의 정보를 입력한다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}