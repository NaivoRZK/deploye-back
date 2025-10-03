from rest_framework import serializers
from .models.reseauSociaux import ReseauSociaux  # recuperation de modele sur agenda.py


class ReseauSociauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseauSociaux
        fields = [
            "id_reseau", "link", "nom_rs"
        ]
        read_only_fields = ["id_reseau", "nom_rs"]
