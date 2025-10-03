from django.db import models
# from .formation import Formation

class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key = True )
    date_formation = models.DateField(default = False)
    id_formation = models.ForeignKey("formation.Formation", on_delete = models.CASCADE, related_name= "agenda")

    def __str__(self):
        return f"{self.id_agenda} {self.date_formation}"
