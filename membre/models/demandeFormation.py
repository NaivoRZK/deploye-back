from django.db import models
# from .membre import Membre

class DemandeFormation(models.Model):
    id_dFormation = models.AutoField(primary_key=True)
    nom_formation = models.CharField(default="", max_length=255)
    description_formation = models.CharField(default="", max_length=500)
    date_formation = models.DateField(null=True, blank=True)  # pas default=""
    duree_formation = models.CharField(default="", max_length=50)
    id_membre = models.ForeignKey(
        'membre.Membre', 
        on_delete=models.CASCADE, 
        related_name="demandes_formation"
    )

    def __str__(self):
        return f"{self.id_dFormation} {self.nom_formation}"
