from django.urls import path
from users.views import UserUpdateAPIView, UserCreateAPIView, UserRetrieveAPIView, UserDestroyAPIView, UserListAPIView

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/', UserListAPIView.as_view(), name='user'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-get'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]