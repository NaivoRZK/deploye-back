from django.db import models
class Partner(models.Model):
    id_partner = models.AutoField(primary_key = True )
    name = models.CharField(default = "")
    Attribute = models.CharField(default = "")
    
    def __str__(self):
        return f"{self.name} {self.Attribute}"
