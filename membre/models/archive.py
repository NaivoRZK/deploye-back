from django.db import models
from .badge import Badge
class Archive(models.Model):
    id_archive = models.AutoField(primary_key = True )
    motif = models.CharField(default = "")
    date_archivage = models.DateField(default = False)
    id_badge = models.ForeignKey('membre.Badge', on_delete = models.CASCADE, related_name = "archives")

    def __str__(self):
        return f"{self.id_archive} {self.motif}"
