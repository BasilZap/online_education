from django.contrib import admin

from univer.models import Lesson, Course, Subscription, Payments


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description', 'image', 'link', 'owner')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'owner')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('course', 'user')


@admin.register(Payments)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'pay_user', 'pay_date', 'payd_course', 'payd_lesson', 'pay_amount', 'pay_method', 'pay_id', 'pay_status')
