from django.db.models.signals import post_save
from django.dispatch import receiver
from vehicles.models import Vehicle
from vehicles.tasks import complete_vehicle_data


@receiver(post_save, sender=Vehicle)
def complete_vehicle_data_post_save(sender, instance, created, **kwargs):
    if created and not instance.brand or not instance.model or not instance.color:
        """se o vehicle foi criado, e os campos: o brand ou model 
        ou color estiverem None, irá rodar esse if."""
        complete_vehicle_data.delay(instance.license_plate)