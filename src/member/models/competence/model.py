from django.db import models

class competence(models.Model):
    id_competence = models.AutoField(primary_key= True)
    # id_member = models.ForeignKey()
    soft = models.CharField(default = False)
    hard = models.CharField(default = False)
    fonction = models.CharField(default = False)
    
    def __str__(self):
        return f"{self.soft} {self.hard}"
