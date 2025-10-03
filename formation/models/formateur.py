from django.db import models

class Formateur(models.Model):
    id_formateur = models.AutoField(primary_key=True)
    nom_formateur = models.CharField(default="", max_length=255)
    prenom_formateur = models.CharField(default="", max_length=255)
    id_membre = models.ForeignKey(
        "membre.Membre",
        on_delete=models.CASCADE,
        related_name="formateur",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.nom_formateur} {self.id_membre}"
