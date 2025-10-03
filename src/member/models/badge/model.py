from django.db import models
class badge(models.Model):
    id_badge = models.AutoField(primary_key = True )
    # id_member = models.ForeignKey()
    # qr_code = models. -> byte 
    date_generation = models.DateField(default = False)
    # format_pdf = models. -> byte 
    
    def __str__(self):
        return f"{self.date_generation} {self.id_badge}"
