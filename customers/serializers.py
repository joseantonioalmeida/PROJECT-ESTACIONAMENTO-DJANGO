from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'cpf', 'phone', 'created_at', 'updated_at']

    user = serializers.StringRelatedField(read_only=True)