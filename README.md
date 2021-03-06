# YaMDb API


## Описание

Учебный проект создания API для базы данных произведений с отзывами и комментариями. Позволяет делать запросы к ресурсам БД с любого устройства.

## Установка

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/isBlueTip/yatube_yamdb.git
```

```
cd yatube_yamdb
```

Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
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
python3 yatube_yamdb/manage.py migrate
```

Запустить проект:

```
python3 yatube_yamdb/manage.py runserver
```

## Права на использование API

- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

- **Аутентифицированный пользователь** *(user)* —  может просматривать описания произведений, читать отзывы и комментарии. Может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.

- **Модератор** *(moderator)* — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- **Администратор** *(admin)* — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Суперюзер Django** — обладет правами администратора *(admin)*.

## Виды запросов к API

1. Эндпойнт http://127.0.0.1:8000/api/v1/auth/signup/
    - POST - регистрация пользователя через *username* и *email*. На почту отправляется код подтверждения *confirmation_code*
2. Эндпойнт http://127.0.0.1:8000/api/v1/auth/token/
    - POST - получение JWT-токена в обмен на *username* и *confirmation code*
3. Эндпойнт http://127.0.0.1:8000/api/v1/categories/
    - GET - получить список всех категорий
    - POST - добавление новой категории
4. Эндпойнт http://127.0.0.1:8000/api/v1/categories/{slug}/
    - DELETE - удаление категории
5. Эндпойнт http://127.0.0.1:8000/api/v1/genres/
    - GET - получение списка всех жанров
    - POST - добавление нового жанра
6. Эндпойнт http://127.0.0.1:8000/api/v1/genres/{slug}/
    - DELETE - удаление жанра
7. Эндпойнт http://127.0.0.1:8000/api/v1/titles/
    - GET - получение списка всех произведений
    - POST - добавить новое произведение
8. Эндпойнт http://127.0.0.1:8000/api/v1/titles/{titles_id}/
    - GET - получение информации о произведении
    - PATCH - частичное обновление информации о произведении
    - DELETE - удаление произведения
9.  Эндпойнт http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
    - GET - получение списка всех отзывов
    - POST - добавление нового отзыва (пользователь может оставить только один отзыв на произведение)
10.  Эндпойнт http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/
    - GET - получить отзыв по id для указанного произведения
    - PATCH - частичное обновление отзыва по id
    - DELETE - удаление отзыва по id
11. Эндпойнт http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
    - GET - получение списка всех комментариев к отзыву
    - POST - добавление комментария к отзыву
12. Эндпойнт http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
    - GET - получение комментария для отзыва по id
    - PATCH - частичное обновление комментария к отзыву id
    - DELETE - удаление комментария по id
13. Эндпойнт http://127.0.0.1:8000/api/v1/users/
    - GET - получение списка всех пользователей
    - POST - добавление нового пользователя
14. Эндпойнт http://127.0.0.1:8000/api/v1/users/{username}/
    - GET - получение пользователя по username
    - PATCH - изменение данных пользователя по username
    - DELETE - удаление пользователя по username
15. Эндпойнт http://127.0.0.1:8000/api/v1/users/me/
    - GET - получение данных своей учетной записи
    - PATCH - изменение данных своей учетной записи

## Авторы
**Руслан Смирнов**

[Email](bludstainz@yandex.ru)  
[Telegram](https://t.me/tiredruslan)

**Семён Егоров**

[LinkedIn](https://www.linkedin.com/in/simonegorov/)  
[Email](rhinorofl@gmail.com)  
[Telegram](https://t.me/SamePersoon)

**Юлия Васильева**

[Email](julka3561@yandex.ru)  
[Telegram](https://t.me/julka3561)
