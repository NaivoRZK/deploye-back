from django.db import models
# from .membre import Membre

class DemandeFormation(models.Model):
    id_dFormation = models.AutoField(primary_key = True )
    nom_formation = models.CharField(default = "")
    description_formation = models.CharField(default = "")
    date_formation = models.DateField(default = "")
    duree_formation = models.CharField(default="")
    id_membre = models.ForeignKey('membre.Membre', on_delete = models.CASCADE, related_name = "DemandeFormation")

    def __str__(self):
        return f"{self.id_dFormation} {self.nom_formation}"
