from django.db import models
# from formation.models.formation import Formation

class Presence(models.Model):
    id_presence = models.AutoField(primary_key = True )
    presence = models.CharField(default = "")
    activite = models.CharField(default = "")
    date = models.DateField(default = False)
    heure = models.CharField(default = "")
    id_formation = models.ForeignKey('formation.Formation', on_delete = models.CASCADE, related_name = "presences")

    def __str__(self):
        return f"{self.id_presence} {self.presence}"
