import smtplib

import stripe
from django.core.mail import send_mail

from config.settings import STRIPE_API_KEY, EMAIL_HOST_USER

stripe.api_key = STRIPE_API_KEY


def stripe_pay(pay_amount):
    """
    Функция формирования счета в Stripe API
    :param pay_amount: Цена -> int
    :return: id счета - > str
    """
    pay = stripe.PaymentIntent.create(
            amount=pay_amount,
            currency="usd",
            automatic_payment_methods={"enabled": True, 'allow_redirects': 'never'},
            payment_method="pm_card_visa"
        )

    # Подтверждение платежа для тестирования
    # stripe.PaymentIntent.confirm(
    #     pay['id'],
    #     payment_method="pm_card_visa",
    # )

    return pay['id']


def stripe_get_success(pay_id):
    """
    Проверка оплаты счета в Stripe API
    :param pay_id: id счета -> str
    :return: статус оплаты - str
    """
    pay_state = stripe.PaymentIntent.retrieve(
        pay_id,
    )
    return pay_state.status


def send_mail_to_user(user_mail: str, message_title: str, user_message: str):
    """
    Отправка email пользователю
    :param user_mail: почтовый адрес -> str
    :param message_title: заголовок сообщения -> str
    :param user_message: сообщение пользователю -> str
    :return: None
    """
    try:
        send_mail(
            subject=message_title,
            message=user_message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[user_mail]
        )  # Отправляем email с указанным сообщением
    except smtplib.SMTPException as mail_error:
        print(mail_error)
