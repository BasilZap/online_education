from django.urls import path
from users.views import UserUpdateAPIView, UserCreateAPIView, UserRetrieveAPIView, UserDestroyAPIView, UserListAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/', UserListAPIView.as_view(), name='user'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-get'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
