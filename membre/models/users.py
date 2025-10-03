from django.db import models
class Users(models.Model):
    id_users = models.AutoField(primary_key = True )
    login = models.CharField(default = "")
    password= models.CharField(default = "")
    # role= models.ForeignKey()
    
    def __str__(self):
        return f"{self.id_users} {self.login}"
