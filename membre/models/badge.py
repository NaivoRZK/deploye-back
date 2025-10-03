from django.db import models
# from .membre import Membre
class Badge(models.Model):
    id_badge = models.AutoField(primary_key = True )
    id_membre = models.ForeignKey('membre.Membre', on_delete = models.CASCADE, related_name = "badges")
    qrcode = models.CharField(default="")         # à discuter selon bibliothèque
    date_generation = models.DateField(default = False)
    
    def __str__(self):
        return f"{self.id_badge} {self.date_generation}"
