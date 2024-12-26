"""
    Serializers for the API View
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from rest_framework import serializers
from django.utils.translation import gettext as _

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for the User Object. """

    class Meta:
        """ Meta class for the UserSerializer. """
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {"password":{"write_only":True, "min_length":8}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    """ Serializer for the user authentication token. """

    email = serializers.EmailField()
    password = serializers.CharField(
        style = {input: "password"},
        trim_whitespace = False
    )

    def validate(self, attrs):
        """ Validate and authenticate the user. """
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            email = email,
            password = password
        )

        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
