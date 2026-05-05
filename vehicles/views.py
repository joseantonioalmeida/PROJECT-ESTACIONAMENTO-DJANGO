from rest_framework.viewsets import ModelViewSet
from vehicles.models import VehicleType, Vehicle
from vehicles.serializers import VehicleTypeSerializer, VehicleSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerOfVehicleOrRecord


class VehicleTypeViewSet(ModelViewSet):
    queryset = VehicleType.objects.all().order_by('-id')
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all().order_by('-id')
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
    