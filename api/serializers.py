# serializers.py
from rest_framework import serializers
from .models import Student  # Replace with your actual model

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # or specify the fields you want to include, e.g., ['id', 'name', 'age']
