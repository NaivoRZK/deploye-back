from rest_framework import serializers
from .models.demandeFormation import DemandeFormation  # recuperation de modele sur agenda.py


class DemandeFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeFormation
        fields = [
            "id_dFormation", "nom_formation", "description_formation", 
            "date_formation", "duree_formation", "id_membre"
        ]
        read_only_fields = ["id_dFormation", "nom_formation"]
