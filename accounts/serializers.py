from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Employee
        fields = ['id', 'email', 'first_name', 'last_name']
        read_only_fields = ['first_name', 'last_name']

    def create(self, validated_data):
        email = validated_data.pop('email')
        user = get_user_model().objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError(
                {"email": "Employee with this email does not exist."}
            )
        return Employee.objects.create(user=user, **validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['email'] = instance.user.email
        return representation


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
