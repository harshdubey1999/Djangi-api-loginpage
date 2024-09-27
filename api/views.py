# views.py
from rest_framework.generics import ListAPIView
from .models import Student  # Replace with your actual model
from .serializers import StudentSerializer  # Import the serializer

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
