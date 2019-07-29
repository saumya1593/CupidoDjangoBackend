from rest_framework_mongoengine import serializers
from cupido.models import employee_details

class EmployeeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = employee_details
        fields = '__all__'