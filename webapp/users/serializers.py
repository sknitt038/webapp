from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    """ user profiles converted into object into json"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'mobile_number', 'address', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            mobile_number=validated_data['mobile_number'],
            address=validated_data['address'],
            password=validated_data['password']

        )

        return user

