from rest_framework import serializers
from vehicles.models import VehicleType, Vehicle


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['id','name', 'description']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_type', 'license_plate', 'brand', 'model', 
                  'color', 'owner', 'created_at', 'updated_at'
        ]