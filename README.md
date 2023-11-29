Персональная лента событий. Лента агригируется из заметок, ачивок, рекламы

## Установка
Склонируйте репозиторий
```
git clone https://github.com/kivaiko/personal_feed.git
```
Перейдите в папку с проектом
```
cd drf_test
```
Установка зависимостей проекта и виртуального окружения
```
poetry install
```
Создайте базу данных PosetgeSQL и измените на свои значения в файле settings
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbname',
        'USER': 'username',
        'PASSWORD': 'userpassword',
        'HOST': '',
        'PORT': '',
    }
}
```
Выполните миграции
```
python manage.py makemigrations
python manage.py migrate  
```
В директории проекта воспользуйтесь командой `python seed.py` , чтобы создать 2 тестовых пользователя и 3 ачивки


**user1** с паролем **password123** является суперюзером
его можно использоваться для входа в админку

Запустите проект
```
python manage.py runserver
```

Для получения ленты пользователя нужно выполнить запрос
http://127.0.0.1:8000/api/feed/?user_id=1

Для поиска по ленте 
http://127.0.0.1:8000/api/feed/?user_id=1&title=note