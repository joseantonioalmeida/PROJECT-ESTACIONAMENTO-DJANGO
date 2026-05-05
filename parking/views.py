from rest_framework.viewsets import ModelViewSet
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer
from rest_framework.permissions import DjangoModelPermissions
from core.permissions import IsOwnerOfVehicleOrRecord
from parking.filters import ParkingRecordFilterClass, ParkingSpotFilterClass


class ParkingSpotViewSet(ModelViewSet):
    queryset = ParkingSpot.objects.all().order_by('-id')
    serializer_class = ParkingSpotSerializer
    rql_filter_class = ParkingSpotFilterClass
    permission_classes = [DjangoModelPermissions]

class ParkingRecordViewSet(ModelViewSet):
    queryset = ParkingRecord.objects.all().order_by('-id')
    serializer_class = ParkingRecordSerializer
    rql_filter_class = ParkingRecordFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)