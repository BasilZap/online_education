from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from univer.paginators import UniverPaginator
from univer.permissions import IsOwner, IsManager, IsManagerOrIsOwner

from univer.models import Course, Lesson, Payments, Subscription
from univer.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer, SubscriptionSerializer
from univer.services import stripe_pay, stripe_get_success


class CourseViewSet(viewsets.ModelViewSet):
    """ Вьюсет для курса """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = UniverPaginator

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


class LessonCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания урока """
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


class LessonListAPIView(generics.ListAPIView):
    """ Контроллер отображения уроков """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = UniverPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер отображения урока """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManagerOrIsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер изменения урока """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManagerOrIsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер удаления урока """
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания подписки"""
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        """
        Метод присваивания подписки пользователю
        :param serializer: Сериализатор
        :return: None
        """
        new_subscribe = serializer.save()
        new_subscribe.user = self.request.user
        new_subscribe.save()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер удаления подписки """
    queryset = Subscription.objects.all()


class PaymentsCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания оплаты """
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        """
        Создание платежа
        :param serializer: PaymentsSerializer
        :return: Объект класса "Платеж"
        """
        new_payment = serializer.save()
        amount = new_payment.pay_amount

        # Вызов функции создания счета, сохраняем id платежа
        new_payment.pay_id = stripe_pay(amount)
        new_payment.save()


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер просмотра оплаты """
    serializer_class = PaymentsSerializer
    permission_classes = [IsManagerOrIsOwner]
    queryset = Payments.objects.all()

    def get_object(self):
        """
        Получение представления объекта для просмотра
        (переопределение метода)
        :return: объект класса "Платеж"
        """
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])

        # Проверка на то, что указана оплата безналичными и не оплачено
        if obj.pay_status == "not_paid" and obj.pay_method == 'transfer':

            # Вызов функции проверки оплаты
            pay_status = stripe_get_success(obj.pay_id)

            # Если оплата подтверждена выставляем статус оплаты в "Оплачено"
            if pay_status == 'succeeded':
                obj.pay_status = 'success'
                obj.save()
        self.check_object_permissions(self.request, obj)
        return obj


# Контроллер вывода платежей
class PaymentsListAPIView(generics.ListAPIView):
    """ Контроллер списка платежей """
    serializer_class = PaymentsSerializer
    permission_classes = [IsManagerOrIsOwner]
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payd_course', 'payd_lesson', 'pay_method')
    ordering_fields = ('pay_date',)



