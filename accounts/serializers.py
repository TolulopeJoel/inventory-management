from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    employee_email = serializers.EmailField(write_only=True)
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'employee_email', 'first_name', 'last_name', 'email',]
        read_only_fields = ['first_name', 'last_name']

    def get_email(self, obj):
        return obj.user.email

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def create(self, validated_data):
        email = validated_data.pop('employee_email')
        user = get_user_model().objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError(
                {"email": "User with this email does not exist."}
            )

        if hasattr(user, 'employee'):
            raise serializers.ValidationError(
                {"email": f"{user.first_name} {user.last_name} is already an employee."}
            )

        return Employee.objects.create(user=user, **validated_data)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords do not match."}
            )
        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
