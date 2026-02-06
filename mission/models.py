from django.db import models

from professional.models import OperatorProfessional, OperatorFleet

class Mission(models.Model):
    mission_date = models.DateField(verbose_name="Data da Missão")
    description = models.TextField(max_length=1000, verbose_name="Descrição")
    operator_professional = models.ForeignKey(
        OperatorProfessional,
        on_delete=models.DO_NOTHING,
        verbose_name="Profissional Alocado",
        related_name="professional_missions"
    ),
    operator_fleet = models.ForeignKey(
        OperatorFleet,
        on_delete=models.DO_NOTHING,
        verbose_name="Frota Alocada",
        related_name="fleet_missions"
    )
    status = models.CharField(
        choices=[
            ("Em execução", "Em execução"),
            ("Finalizada", "Finalizada")
        ]
    )

    def __str__(self):
        return f"{self.mission_date} - {self.operator_professional} - {self.operator_fleet} - {self.status}"

    class Meta:
        verbose_name = "Missão"
        verbose_name_plural = "Missões"
