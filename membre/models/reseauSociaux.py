from django.db import models
class ReseauSociaux(models.Model):
    id_reseau = models.AutoField(primary_key = True )
    link = models.CharField(default = "")
    nom_rs = models.CharField(default = "")
    
    def __str__(self):
        return f"{self.id_reseau} {self.nom_rs}"
