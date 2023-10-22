from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        """
        Проверка состоит ли пользователь в группе менеджеров
        :param request: Запрос
        :param view: Контроллер
        :return: Bool
        """
        r_user = request.user
        return r_user.groups.filter(name='manager').exists()


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        """
        Проверка, является ли пользователь создателем курса/урока
        :param request: Запрос
        :param view: Контроллер
        :return: Bool
        """
        return request.user == view.get_object().owner


class IsManagerOrIsOwner(BasePermission):
    def has_permission(self, request, view):
        """
        Проверка является ли пользователь создателем или состоит в группе менеджеры
        :param request: Запрос
        :param view: Контроллер
        :return: Bool
        """
        if request.user.groups.filter(name='manager').exists() or request.user.is_superuser:
            return True
        return request.user == view.get_object().owner
