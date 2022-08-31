from api.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Employee
        fields = "__all__"

