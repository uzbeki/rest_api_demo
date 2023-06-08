# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api_app.models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = "__all__"