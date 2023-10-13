from rest_framework import serializers

from univer.serializers import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = ('id', 'payments', 'first_name', 'last_name', 'email', 'phone', 'city', 'avatar')

