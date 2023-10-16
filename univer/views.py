from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from univer.permissions import IsOwner, IsManager, IsManagerOrIsOwner

from univer.models import Course, Lesson, Payments, Subscription
from univer.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer


# Вьюсет для курса
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    action_permissions = {
        'create': [~IsManager],
        'destroy': [IsOwner],
        'update': [IsManagerOrIsOwner],
        'partial_update': [IsManagerOrIsOwner],
        'retrieve': [IsAuthenticated],
        'list': [IsAuthenticated]
    }

    def get_permissions(self):
        """
        Метод возвращает разрешение для каждого действия ViewSet
        :return:
        """
        return [permission() for permission in self.action_permissions[self.action]]


    def perform_create(self, serializer):
        """
        Метод присвоения владельца каждому курсу
        :param serializer: Сериализатор
        :return: None
        """
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


# Контроллер создания урока
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsManager]

    def perform_create(self, serializer):
        """
        Метод присвоения владельца каждому уроку
        :param serializer: Сериализатор
        :return: None
        :param serializer:
        :return:
        """
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


# Контроллер отображения уроков
class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


# Контроллер отображения урока
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManagerOrIsOwner]


# Контроллер изменения урока
class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManagerOrIsOwner]


# Контроллер удаления урока
class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


# Контроллер вывода платежей
class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payd_course', 'payd_lesson', 'pay_method')
    ordering_fields = ('pay_date',)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        """
        Метод присваивания подписки пользователю
        :param serializer: Сериализатор
        :return: None
        :param serializer:
        :return:
        """
        new_subscribe = serializer.save()
        new_subscribe.user = self.request.user
        new_subscribe.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()

