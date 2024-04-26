from rest_framework import serializers
from .models import Employee, Locations

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['employee', 'address', 'city', 'state', 'country', 'postal_code']

class EmployeeSerializer(serializers.ModelSerializer):
    location = LocationsSerializer(many = True, read_only = True)
    class Meta:
        model = Employee
        fields = ['empid', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary', 'department','location']
