from django.db import models
# from .presence import Presence
# from .reseauSociaux import ReseauSociaux
# from .archive import Archive
# from .stack import Stack
# from .avertisement import Avertisement

class Membre(models.Model):
    id_membre = models.AutoField(primary_key=True)
    
    nom = models.CharField(max_length=100, default="")
    prenom = models.CharField(max_length=100, default="")
    image = models.FileField(null=True, blank=True)  # FileField ne doit pas avoir default=None
    inscription_date = models.DateField(null=True, blank=True)  # pas default=False, ça pose problème
    badge_status = models.BooleanField(default=False)
    address = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=20, default="")
    sexe = models.CharField(max_length=10, default="")
    occupation = models.CharField(max_length=100, default="")
    niveau_etude = models.CharField(max_length=50, default="")
    ecole = models.CharField(max_length=100, default="")
    role = models.CharField(max_length=50, default="")

    # Relations
    id_presence = models.ForeignKey('membre.Presence', on_delete=models.CASCADE, related_name="membres")
    id_reseau = models.ForeignKey('membre.ReseauSociaux', on_delete=models.CASCADE, related_name="membres")
    id_stack = models.ForeignKey('membre.Stack', on_delete=models.CASCADE, related_name="membres")
    id_archive = models.ForeignKey('membre.Archive', on_delete=models.CASCADE, related_name="membres")
    id_avertissement = models.ForeignKey('membre.Avertissement', on_delete=models.CASCADE, related_name="membres")

    def __str__(self):
        return f"{self.id_membre} {self.nom}"
