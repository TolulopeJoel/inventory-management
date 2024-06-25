from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, UserRegistrationAPIView

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
]


urlpatterns += router.urls
