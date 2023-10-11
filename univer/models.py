from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    image = models.ImageField(upload_to='univer/', verbose_name='Фото', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='название курса')
    description = models.TextField(verbose_name='описание курса')
    image = models.ImageField(upload_to='lesson/', verbose_name='Фото', **NULLABLE)
    link = models.TextField(verbose_name='ссылка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
