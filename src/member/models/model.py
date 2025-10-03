from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Champs de base hérités de AbstractUser :
    # username, email, password, first_name, last_name, etc.
    # Tu peux personnaliser / override si besoin.

    id_member = models.AutoField(primary_key=True)  # identifiant unique
    first_name = models.CharField(max_length=150)  # déjà présent dans AbstractUser, mais tu peux redéfinir
    last_name = models.CharField(max_length=150)   # idem
    image = models.ImageField(upload_to="members/", blank=True, null=True)
    inscription_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)  # actif ou non
    badge_status = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(
        max_length=10,
        choices=[("M", "Masculin"), ("F", "Féminin"), ("A", "Autre")],
        blank=True,
        null=True
    )
    # Si tu veux stocker plusieurs rôles → ManyToManyField ou ArrayField (PostgreSQL)
    role = models.JSONField(default=list, blank=True)  
    detail_status = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


