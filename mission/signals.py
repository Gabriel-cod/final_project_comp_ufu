from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Mission
from professional.models import OperatorProfessional, OperatorFleet, Status


@receiver(post_save, sender=Mission)
def update_operator_status(sender, instance, **kwargs):
    fleets = instance.operator_fleet.all()
    professionals = instance.operator_professional.all()
    if instance.status == 'Finalizada':

        available_status = Status.objects.filter(status_name='Disponivel').first()

        for fleet in fleets:
            fleet.status = available_status
            fleet.save()

        for professional in professionals:
            professional.status = available_status
            professional.save()

    else:
        ocupied_status = Status.objects.filter(status_name='Alocado').first()
        for fleet in fleets:
            fleet.status = ocupied_status
            fleet.save()

        for professional in professionals:
            professional.status = ocupied_status
            professional.save()