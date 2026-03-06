from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

from .models import Mission
from professional.models import OperatorProfessional, OperatorFleet, Status


def update_related_statuses(mission):
    fleets = mission.operator_fleet.all()
    professionals = mission.operator_professional.all()

    # Define qual status buscar baseado no status da missão
    # Nota: Se 'status' na Mission for uma ForeignKey, talvez você precise usar mission.status.status_name == 'Finalizada'
    if mission.status == 'Finalizada':
        target_status = Status.objects.filter(status_name='Disponivel').first()
    else:
        target_status = Status.objects.filter(status_name='Alocado').first()

    if target_status:
        # Atualiza Frotas (usando update_fields por performance)
        for fleet in fleets:
            if fleet.status != target_status:
                fleet.status = target_status
                fleet.save(update_fields=['status'])

        # Atualiza Profissionais
        for professional in professionals:
            if professional.status != target_status:
                professional.status = target_status
                professional.save(update_fields=['status'])


# 1. Sinal acionado ao salvar/atualizar a Missão (Ex: Mudou o status de 'Em execução' para 'Finalizada')
@receiver(post_save, sender=Mission)
def update_operator_status_on_mission_save(sender, instance, created, **kwargs):
    # Executamos a lógica sempre. Na criação, os M2M estarão vazios aqui, 
    # mas o m2m_changed vai cobrir isso na sequência.
    update_related_statuses(instance)


# 2. Sinal acionado quando Frotas ou Profissionais são adicionados/removidos da Missão
@receiver(m2m_changed, sender=Mission.operator_fleet.through)
@receiver(m2m_changed, sender=Mission.operator_professional.through)
def update_operator_status_on_m2m_change(sender, instance, action, **kwargs):
    # O 'post_add' garante que os itens já foram salvos na tabela intermediária
    if action in ['post_add', 'post_remove', 'post_clear']:
        update_related_statuses(instance)