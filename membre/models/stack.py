from django.db import models
class Stack(models.Model):
    id_stack = models.AutoField(primary_key = True )
    nom_stack = models.CharField(default = "")
    hard = models.CharField(default = "")
    soft = models.CharField(default = "")
    
    def __str__(self):
        return f"{self.id_stack} {self.nom_stack}"
