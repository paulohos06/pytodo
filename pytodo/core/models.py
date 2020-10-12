from django.db import models


# Create your models here.
class Activity(models.Model):
    STATUS_CHOICES = [
        ("C", "Concluída"),
        ("E", "Em Execução"),
        ("R", "Rejeitada"),
    ]

    num_act = models.CharField(
        "demanda",
        max_length=30,
        blank=True,
        help_text="Identificação da atividade.",
    )
    system_name = models.CharField(
        "sistema", max_length=10, blank=True, help_text="Sigla do sistema."
    )
    description = models.TextField(
        "descrição",
        max_length=100,
        help_text="Descrição sobre o que deve ser feito na atividade.",
    )
    date_act = models.DateTimeField(
        "data", help_text="A data em que a atividade foi realizada."
    )
    status = models.CharField(
        "status",
        max_length=1,
        blank=True,
        choices=STATUS_CHOICES,
        help_text="Flag para indicar qual a situação da atividade.",
    )
    comment = models.TextField(
        "comentário",
        max_length=4000,
        blank=True,
        help_text="Comentários sobre o que foi feito na atividade.",
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)

    def __str__(self):
        return f"{self.system_name} - {self.num_act}"

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ("-date_act",)
