from django.db import models


# table presence 
class presence(models.Model):
    id_presence = models.AutoField(primary_key= True) # identifiant unique
    presence = models.BooleanField(default= True)
    activite = models.CharField(default= False)
    # cours = models. -> byte 
    date = models.DateField(default= False)
    
    def __str__(self):
        return f"{self.activite} {self.date}"
