# api/serializers.py
from rest_framework import serializers
from myauth.models import User
from .models import Organisation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'firstName', 'lastName', 'email', 'phone']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['userId'] = str(instance.userId)  # Ensure UUID is converted to string
        return rep
 
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['org_id', 'name', 'description']


class OrganizationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name', 'description']

    def create(self, validated_data):
        organization = Organisation.objects.create(**validated_data)
        return organization