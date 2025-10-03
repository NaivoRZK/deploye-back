from django.db import models

class Partner(models.Model):
    id_partner = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=255)
    Attribute = models.CharField(default="", max_length=255)
    
    def __str__(self):
        return f"{self.name} {self.Attribute}"
