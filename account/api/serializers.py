from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['ip_nalog']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'is_active', 'email', 'profile']
