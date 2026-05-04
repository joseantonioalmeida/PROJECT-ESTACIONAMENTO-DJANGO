from rest_framework import serializers
from parking.models import ParkingRecord, ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingSpot
        fields = ['id', 'spot_number', 'is_occupied', 
                  'created_at', 'updated_at'
        ]


class ParkingRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParkingRecord
        fields = ['id', 'vehicle', 'parking_spot', 'entry_time', 'exit_time', 
                  'created_at', 'updated_at',
        ]