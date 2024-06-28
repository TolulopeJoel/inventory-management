from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeeSerializer, UserRegistrationSerializer


class EmployeeViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class UserRegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
