from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from univer.models import Course, Lesson, Payments
from univer.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer


# Вьюсет для курса
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# Контроллер создания урока
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


# Контроллер отображения уроков
class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# Контроллер отображения урока
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# Контроллер изменения урока
class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# Контроллер удаления урока
class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


# Контроллер вывода платежей
class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payd_course', 'payd_lesson', 'pay_method')
    ordering_fields = ('pay_date',)
