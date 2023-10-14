from rest_framework import serializers

from univer.models import Course, Lesson, Payments


# Сериализатор для урока
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


# Сериализатор для курса
class CourseSerializer(serializers.ModelSerializer):
    course_lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_course_lesson_count(self, course):
        """
        Метод вывода уроков конкретного курса
        :param course: Курс
        :return: счетчик int
        """
        return Lesson.objects.filter(course=course).count()


# Сериализатор для платежей
class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
