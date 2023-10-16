from rest_framework import serializers

from univer.models import Course, Lesson, Payments, Subscription
from univer.validators import LinkValidator


# Сериализатор для урока
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]


# Сериализатор для курса
class CourseSerializer(serializers.ModelSerializer):
    course_lesson_count = serializers.SerializerMethodField()
    subscribed = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_course_lesson_count(self, course):
        """
        Метод вывода количества уроков конкретного курса
        :param course: Курс
        :return: счетчик int
        """
        return Lesson.objects.filter(course=course).count()

    def get_subscribed(self, course):
        """
        Метод ищет экземпляр класса "Подписка" с заданными
        значениями полей
        :param course: Курс
        :return: статус "Подписан/Не подписан" -> str
        """
        request = self.context.get('request')
        is_subscribed = Subscription.objects.filter(user=request.user, course=course).exists()
        if not is_subscribed:
            return 'Не подписан'
        return 'Подписан'


# Сериализатор для платежей
class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
