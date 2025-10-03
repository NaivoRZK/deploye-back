from django.db import models

class Users(models.Model):
    id_users = models.AutoField(primary_key=True)
    login = models.CharField(default="", max_length=150)
    password = models.CharField(default="", max_length=128)
    # role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.id_users} {self.login}"
