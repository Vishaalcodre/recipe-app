"""
    Serializers for the API View
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the User Object. """

    class Meta:
        """ Meta class for the UserSerializer. """
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {"password":{"write_only":True, "min_length":8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)