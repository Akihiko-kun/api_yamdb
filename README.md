# api_yamdb
api_yamdb

## Описание:
```
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся,
здесь нельзя посмотреть фильм или послушать музыку.
```
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Akihiko-kun/api_yamdb.git
```

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

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

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
