from rest_framework.viewsets import ModelViewSet
from vehicles.models import VehicleType, Vehicle
from vehicles.serializers import VehicleTypeSerializer, VehicleSerializer


class VehicleTypeViewSet(ModelViewSet):
    queryset = VehicleType.objects.all().order_by('-id')
    serializer_class = VehicleTypeSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all().order_by('-id')
    serializer_class = VehicleSerializer