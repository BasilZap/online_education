from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from univer.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """
    Класс тестирования эндпоинтов уроков
    """

    def tearDown(self):
        Course.objects.all().delete()
        Lesson.objects.all().delete()

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='test course',
            description='test course description',
        )
        self.lesson = Lesson.objects.create(
            name='test',
            description='test',
            link='https://www.youtube.com/test'
        )

    def test_create_lesson(self):
        """
        Метод тестирования эндпоинта создания урока
        :return:
        """
        data = {
            "name": "test lesson",
            "description": "test lesson description",
            "link": "https://www.youtube.com/test_lesson",
            "course": self.course.pk
        }
        response = self.client.post(
            reverse('univer:lesson-create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )
        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.pk + 1,
                'name': 'test lesson',
                'description': 'test lesson description',
                'image': None,
                'link': 'https://www.youtube.com/test_lesson',
                'course': self.course.pk,
                'owner': 1
            }
        )

    def test_list_lesson(self):
        """
        Метод тестирования эндпоинта вывода списка уроков
        :return:
        """
        response = self.client.get(
            reverse('univer:lesson'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [
                {
                    'id': self.lesson.pk,
                    'name': 'test',
                    'description': 'test',
                    'image': None,
                    'link': 'https://www.youtube.com/test',
                    'course': None,
                    'owner': None

                }
            ]

        )

    def test_update_lesson(self):
        """
        Метод тестирования эндпоинта изменения урока
        :return:
        """
        new_data = {
            "name": "test updated lesson",
            "description": "test updated lesson",
            "link": "https://www.youtube.com/test_lesson"
        }

        response = self.client.put(
            reverse('univer:lesson-update', args=str(self.lesson.pk)),
            data=new_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.pk,
                'name': 'test updated lesson',
                'description': 'test updated lesson',
                'image': None,
                'link': 'https://www.youtube.com/test_lesson',
                'course': None,
                'owner': None
            }
        )

    def test_view_lesson(self):
        """
        Метод тестирования эндпоинта просмотра урока
        :return:
        """
        response = self.client.get(
            reverse('univer:lesson-get', args=str(self.lesson.pk)),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'id': self.lesson.pk,
                'name': self.lesson.name,
                'description': self.lesson.description,
                'image': None,
                'link': self.lesson.link,
                'course': None,
                'owner': None
            }
        )

    def test_delete_lesson(self):
        """
        Метод тестирования эндпоинта удаления урока
        :return:
        """
        response = self.client.delete(
            reverse('univer:lesson-delete', args=str(self.lesson.pk)),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):
    """
    Класс тестирования эндпоинтов подписки
    """

    def tearDown(self):
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Subscription.objects.all().delete()

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='test course',
            description='test course description',
        )

        self.subscription = Subscription.objects.create(
            course=self.course
        )

    def test_create_subscription(self):
        """
        Тестирование эндпоинта добавления подписки
        :return: None
        """
        data = {
            "course": self.course.pk,
            "user": self.user.pk
        }
        response = self.client.post(
            reverse('univer:subscribe'),
            data=data
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            2
        )

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'course': self.course.pk,
                'user': self.user.pk

            }
        )

    def test_delete_subscription(self):
        """
        Тестирование эндпоинта удаления подписки
        :return: None
        """
        response = self.client.delete(
            reverse('univer:unsubscribe', args=str(self.subscription.pk)),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
