import stripe

from config.settings import STRIPE_API_KEY

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
