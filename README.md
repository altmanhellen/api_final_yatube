### Описание

API социальной сети, предназначенной для публикации постов, написания комментариев и возможности подписки на других пользователей. Реализовано: 
- возможность комментирования постов;
- подписка на других авторов;
- регистрация пользователей.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Пример http-запроса

Endpoint: /api/v1/posts/
Method: POST
Body:

```
{
  "username": "best_author",
  "password": "my_secret_qwerty_password"
}
```

Полная документация API доступна по адресу http://127.0.0.1:8000/redoc/.