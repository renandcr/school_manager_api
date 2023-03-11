from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'role', 'date_joined', 'password', 'school' ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data = {**validated_data, 'password': make_password(validated_data['password'])}
        instance = User.objects.create(**validated_data)
        return instance
    
    def update(self, instance: User, validated_data: dict):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.role = validated_data.get('role', instance.role)
        if validated_data.get('password'):
            instance.password = make_password(validated_data['password'])

        instance.save()
        return instance