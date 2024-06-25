from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import EmployeeSerializer, UserRegistrationSerializer


class CreateEmployeeAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = EmployeeSerializer


class UserRegistrationAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

