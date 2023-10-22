from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания пользователя """
    serializer_class = UserSerializer
    permission_classes = [~IsAuthenticated]


class UserListAPIView(generics.ListAPIView):
    """ Контроллер отображения пользователей """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер отображения пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер изменения пользователя """
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Контроллер удаления пользователя
class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
