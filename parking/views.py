from rest_framework.viewsets import ModelViewSet
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer


class ParkingSpotViewSet(ModelViewSet):
    queryset = ParkingSpot.objects.all().order_by('-id')
    serializer_class = ParkingSpotSerializer

class ParkingRecordViewSet(ModelViewSet):
    queryset = ParkingRecord.objects.all().order_by('-id')
    serializer_class = ParkingRecordSerializer