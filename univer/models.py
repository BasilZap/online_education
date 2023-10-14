from django.db import models

from config import settings
from users.models import NULLABLE, User

PAY_METHODS = (
    ('cash', 'наличные'),
    ('transfer', 'безналичный расчет')
)


# Модель 'Курс'
class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    image = models.ImageField(upload_to='univer/', verbose_name='Фото', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


# Модель 'Урок'
class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='название курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')
    image = models.ImageField(upload_to='lesson/', verbose_name='Фото', **NULLABLE)
    link = models.TextField(verbose_name='ссылка')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


# Модель 'Платежи'
class Payments(models.Model):
    pay_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    pay_date = models.DateField(verbose_name='Дата оплаты')
    payd_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE)
    payd_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE)
    pay_amount = models.FloatField(verbose_name='Сумма оплаты', **NULLABLE)
    pay_method = models.CharField(max_length=10, choices=PAY_METHODS, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.pay_user} {self.payd_course if self.payd_course else self.payd_lesson} ' \
               f'оплата {self.pay_amount}: {self.pay_method}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
