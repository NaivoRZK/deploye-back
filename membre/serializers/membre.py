from rest_framework import serializers
from membre.models.membre import Membre  # recuperation de modele sur agenda.py


class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = [
            "id_membre", "nom", "prenom", 
            "image", "inscription_date", "badge_status",
            "address", "phone_number", "sexe",
            "occupation", "niveau_etude", "ecole",
            "role", "id_presence", "id_reseau",
            "id_domaine", "id_archive", "id_avertissement"
        ]
        read_only_fields = ["id_membre", "nom"]
