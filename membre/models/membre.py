from django.db import models
# from .presence import Presence
# from .reseauSociaux import ReseauSociaux
# from .archive import Archive
# from .stack import stack
# from .avertisement import Avertisement

class Membre(models.Model):
    id_membre = models.AutoField(primary_key = True )
    nom = models.CharField(default = "")
    prenom = models.CharField(default = "")
    image = models.FileField(default = None)
    inscription_date = models.DateField(default = False)
    badge_status = models.BooleanField(default = False)
    address = models.CharField(default = "")
    phone_number = models.CharField(default = "")
    sexe = models.CharField(default = "")
    occupation = models.CharField(default = "")
    niveau_etude = models.CharField(default = "")
    ecole = models.CharField(default = "")
    role = models.CharField(default ="")
    # relation 
    id_presence = models.ForeignKey('membre.Presence', on_delete = models.CASCADE, related_name = "membres")
    id_reseau = models.ForeignKey('membre.ReseauSociaux', on_delete = models.CASCADE, related_name = "membres")
    id_stack = models.ForeignKey('membre.Stack', on_delete = models.CASCADE, related_name = "membres")
    id_archive = models.ForeignKey('membre.Archive', on_delete = models.CASCADE, related_name = "membres")
    id_avertissement = models.ForeignKey('membre.Avertissement', on_delete = models.CASCADE, related_name = "membres")

    def __str__(self):
        return f"{self.id_membre} {self.nom}"
