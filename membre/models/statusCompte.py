from django.db import models
# from .membre import Membre

class StatusCompte(models.Model):
    id_statuscompte = models.AutoField(primary_key = True )
    status = models.BooleanField(default = False)
    id_membre = models.ForeignKey('membre.Membre', on_delete = models.CASCADE, related_name = "status_comptes")
    
    def __str__(self):
        return f"{self.id_statuscompte} {self.status}"
