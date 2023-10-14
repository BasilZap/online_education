from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer


# Контроллер создания пользователя
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [~IsAuthenticated]


# Контроллер отображения пользователей
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Контроллер отображения пользователя
class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Контроллер изменения пользователя
class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Контроллер удаления пользователя
class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
