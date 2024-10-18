from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    client = serializers.CharField(source='client.client_name', read_only=True)

    class Meta:
        model = Project
        # fields = ['id', 'project_name', 'client', 'assigned_users', 'created_at', 'created_by']
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Client
        # fields = ['id', 'client_name', 'created_at', 'created_by', 'projects', 'updated_at']
        fields = '__all__'
class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_name']


