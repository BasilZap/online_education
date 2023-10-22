# Домашняя работа 24.1 "Вьюсеты и дженерики".

## Функционал.
### Создан django проект с моделями:
   - Пользователь:
        - все поля от обычного пользователя, но авторизацию заменить на email;
        - телефон;
        - город;
        - аватарка.
   - Курс:
        - название,
        - превью (картинка),
        - описание.
   - Урок:
        - название,
        - описание,
        - превью (картинка),
        - ссылка на видео.

### Описан CRUD:
    
   - Для модели "Курс" через ViewSets
   - Для моделей "Урок" и "Пользователь" через Generics-классы

## Домашняя работа 24.2 "Сериализаторы"

- Добавлена модель "Платежи", таблица заполнена данными.
- Для модели курса в сериализатор добавлено поле вывода количества уроков
- Для сериализатора модели курса реализовано поле вывода уроков.
- Настрокна фильтрация для эндпоинтов вывода списка платежей с возможностями:

     - менять порядок сортировки по дате оплаты,
     - фильтровать по курсу или уроку,
     - фильтровать по способу оплаты.
- Для профиля пользователя сделан вывод истории платежей

## Домашняя работа 25.1 "Права доступа в DRF"
- Настроено использование JWT, закрыты эндпоинты
- Создана группа модераторов, члены которой не могут создавать и удалять курсы и уроки
- Распределены права, чтобы пользователи не входящие в группу модераторов могли изменять только свои уроки и курсы

## Домашняя работа 25.2 "Валидаторы, пагинация и тесты"
- Для сохранения уроков реализована проверка на то, что ролик выложен на youtube
- Реализована модель подписки на обновления курса для пользователя и эндпоинты на добавление и удаление подписки
- Реализован признак подписки для пользователя при выводе курса
- Реализована пагинация для вывода всех уроков и курсов
- Написаны тесты для CRUD уроков и подписки, результат покрытия тестами сохранен в .coverage

## Домашняя работа 26.1 "Документирование и безопасность"
- Подключен и настроен вывод документации для проекта
- Подключить возможность оплаты курсов через https://stripe.com/docs/api, реализовано создание и проверка платежа

### Требования к установке.
- В PostgreSQL должна быть создана DB - univer

Есть возможность заполнить таблицы БД данными:
- Все таблицы:
```
> python manage.py loaddata all.json
```
Администратор - admin@sky.ru; пароль 123456
Модератор - petr.petrov@sky.ru; пароль 123456
Пользователи - sergey.sergeev@sky.ru, ivan.ivanov@sky.ru, aleksey.alekseev@sky.ru; пароли - 123456

#### Альтернативный способ

- Курсы и уроки:
```
> python manage.py loaddata lesson.json
```

- Платежи:
```
> python manage.py loaddata pay.json
```

- Пользователи:
```
> python manage.py loaddata users.json
```
При таком заполнении отдельно в панели администрирования нужно создать группу manager

## Требования к окружению

#### В программе используется менеджер зависимостей venv.
Используются следующие зависимости:

- Django==4.2.4
- ipython==8.14.0
- Pillow==10.0.0
- psycopg2-binary==2.9.7
- pytils==0.4.1
- djangorestframework==3.14.0
- django-filter==23.3
- djangorestframework-simplejwt==5.3.0
- coverage==7.3.2
- drf-yasg==1.21.7
- python-dotenv==1.0.0
- stripe==7.0.0