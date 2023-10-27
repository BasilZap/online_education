import datetime

from celery import shared_task
from django.utils import timezone

from univer.models import Course, Subscription
from univer.services import send_mail_to_user
from users.models import User


@shared_task
def course_change_alert(action: str, course_id: int, lesson_name: str):
    """
    Функция формирования рассылок пользователям,
    подписанным на курс об изменении, добавлении
    или удалении уроков в курсе
    :param action: действие (добавление/изменение/удаление) -> str
    :param course_id: id курса -> int
    :param lesson_name: Название урока -> str
    :return: None
    """
    # Формируем словарь сообщений в зависимости от действия
    course = Course.objects.get(pk=course_id)
    user_message_choice = {'create': f'В курсе - {course.name}, добавлен урок {lesson_name}',
                           'delete': f'Из курса - {course.name}, удален урок {lesson_name}',
                           'update': f'Изменен урок {lesson_name}'}
    message_title = f'Изменение в подписке {course.name}'
    # Ищем подписки на курс
    subscriptions = Subscription.objects.filter(course=course)
    # Если подписки найдены отправляем письма и меняем дату обновления курса на текущую
    if subscriptions:

        date_of_update = timezone.now()
        for subscription in subscriptions:

            # Проверка имени пользователя - указано/не указано
            if subscription.user.username is not None:
                user_name = subscription.user.username
            else:
                user_name = 'подписчик'

            send_mail_to_user(subscription.user.email, message_title, user_message_choice[action])
            user_message = f'Уважаемый {user_name}, {message_title}, {user_message_choice[action]}'
            course.last_update = date_of_update
            course.save()
            print(user_message)


def block_not_active_users():
    """
    Функция, определяющая пользователей, которые
    последний раз заходили более 30 дней назад и если
    такие есть выставляет флаг is_active в False
    :return:
    """
    current_date = timezone.now()
    time_delta = current_date - datetime.timedelta(days=30)
    all_users = User.objects.filter(last_login__lt=time_delta)
    if all_users is not None:
        for usr in all_users:
            usr.is_active = False
            usr.save()
