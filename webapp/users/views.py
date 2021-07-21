from rest_framework import filters
from rest_framework import viewsets
from . import serializers
from . import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'name', 'mobile_number')
