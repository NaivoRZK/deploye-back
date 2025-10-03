from django.db import models

class Stack(models.Model):
    id_stack = models.AutoField(primary_key=True)
    nom_stack = models.CharField(default="", max_length=255)
    hard = models.CharField(default="", max_length=255)
    soft = models.CharField(default="", max_length=255)
    
    def __str__(self):
        return f"{self.id_stack} {self.nom_stack}"
