from django.apps import AppConfig


class VehiclesConfig(AppConfig):
    name = 'vehicles'
    verbose_name = 'Veículos'

    def ready(self) -> None:
        import vehicles.signals