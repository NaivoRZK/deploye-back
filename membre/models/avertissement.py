from django.db import models
# from .membre import Membre
# from .badge import Badge

class Avertissement(models.Model):
    id_avertissement = models.AutoField(primary_key = True )
    nombre_avertissement = models.IntegerField(default = 0)
    id_membre = models.ForeignKey('membre.Membre', on_delete= models.CASCADE)
    id_badge = models.ForeignKey('membre.Badge', on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id_avertissement} {self.nombre_avertissement}"
