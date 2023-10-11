from django.urls import path, include
from rest_framework.routers import DefaultRouter

from univer.apps import UniverConfig
from univer.views import CourseViewSet, LessonRetrieveAPIView, LessonCreateAPIView, LessonListAPIView, \
    LessonDestroyAPIView, LessonUpdateAPIView

app_name = UniverConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
] + router.urls

