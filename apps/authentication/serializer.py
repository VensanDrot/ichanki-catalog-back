from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.authentication.models import User


class JWTObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # token['fullname'] = user.fullname
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'fullname',
                  'username',
                  'is_superuser']


class PostUserSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        instance.set_password(password)
        instance.save()
        return instance

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance: User = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'fullname',
                  'password',
                  'is_superuser']
