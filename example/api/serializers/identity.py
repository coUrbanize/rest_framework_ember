from django.contrib.auth import models as auth_models
from rest_framework_3 import serializers


class IdentitySerializer(serializers.ModelSerializer):
    """
    Identity Serializer
    """
    class Meta:
        model = auth_models.User
        fields = (
            'id', 'first_name', 'last_name', 'email', )

