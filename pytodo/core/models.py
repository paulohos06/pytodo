from django.db import models


# Create your models here.
class Activity(models.Model):
    STATUS_CHOICES = [
        ("C", "Concluída"),
        ("E", "Em Execução"),
        ("R", "Rejeitada"),
    ]

    num_act = models.CharField("demanda", max_length=15)
    system_name = models.CharField("sistema", max_length=10)
    description = models.TextField("descrição", max_length=100)
    date_act = models.DateTimeField(
        "data", help_text="A data em que a atividade foi realizada."
    )
    status = models.CharField(
        "status", max_length=1, blank=True, choices=STATUS_CHOICES
    )
    comment = models.TextField(
        "comentário",
        max_length=4000,
        blank=True,
        help_text="Comentários sobre o que foi feito na atividade.",
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        ordering = ("-date_act",)

        def __str__(self):
            return f"{self.system_name} - {self.num_act}"
