from django.db import models

class Formation(models.Model):
    id_formation = models.AutoField(primary_key=True)
    title = models.CharField(default="", max_length=255)
    description = models.CharField(default="", max_length=500)
    date_formation = models.DateField(null=True, blank=True)  
    duree_formation = models.PositiveIntegerField(
        null=True, blank=True, 
        help_text="Durée de la formation en heures"
    )
    intervenant = models.CharField(default="", max_length=255)

    id_partner = models.ForeignKey(
        'formation.Partner',
        on_delete=models.SET_NULL,
        related_name="formations",
        null=True,
        blank=True,
        default=None
    )
    id_formateur = models.ForeignKey(
        'formation.Formateur',
        on_delete=models.SET_NULL,
        related_name="formations",
        null=True,
        blank=True,
        default=None
    )
    id_membre = models.ForeignKey(
        'membre.Membre',
        on_delete=models.SET_NULL,
        related_name="formations",
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return f"{self.title} {self.date_formation or ''}"
