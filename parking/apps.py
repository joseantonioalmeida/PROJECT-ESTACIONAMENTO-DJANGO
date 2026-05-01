from django.apps import AppConfig


class ParkingConfig(AppConfig):
    name = 'parking'
    verbose_name = 'Registro'

    def ready(self) -> None:
        import parking.signals