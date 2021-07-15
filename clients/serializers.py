from django.utils import timezone
from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'business_owner',
            'first_name',
            'last_name',
            'birthdate',
            'email',
            'phone_number',
            'address',
            'gender',
            'profile_picture'
        )

    def validate(self, data):
        if data['birthdate'] >= timezone.now():
            raise serializers.ValidationError({'birthdate': 'Cannot be in the future'})
        return data
