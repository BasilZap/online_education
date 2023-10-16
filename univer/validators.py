import re

from rest_framework.serializers import ValidationError


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        pattern = re.compile("(www.youtube.|youtu.be)")
        if not pattern.search(field_value):
            raise ValidationError('Некорректная ссылка, материал должен быть выложен на youtube')
