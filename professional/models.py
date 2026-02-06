from django.db import models


class Status(models.Model):
    status_name = models.CharField(max_length=50, verbose_name="Nome do Status")

    def __str__(self):
        return str(self.status_name)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"


class OperatorProfessional(models.Model):
    ROLE_LIST = [
        ("Piloto", "Piloto"),
        ("Bombeiro", "Bombeiro"),
        ("Mecânico", "Mecânico"),
        ("Médico", "Médico"),
        ("Enfermeiro", "Enfermeiro")
    ]

    name = models.CharField(max_length=20, verbose_name="Nome")
    role = models.CharField(choices=ROLE_LIST, verbose_name="Cargo")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"


class OperatorFleet(models.Model):
    fleet_type = models.CharField(max_length=50, verbose_name="Tipo da Frota")
    fleet_model = models.CharField(max_length=50, verbose_name="Modelo da Frota")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.fleet_type} - {self.fleet_model}"

    class Meta:
        verbose_name = "Frota"
        verbose_name_plural = "Frotas"
