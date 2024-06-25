from django.urls import path

from .views import CreateEmployeeAPIView, UserRegistrationAPIView

urlpatterns = [
    path('create-employee/', CreateEmployeeAPIView.as_view(), name='create_employee'),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
]
