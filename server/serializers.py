
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'name', 'value', 'letter', 'student', 'teacher')
