from rest_framework import serializers
from .models.avertissement import Avertissement  # recuperation de modele sur agenda.py


class AvertissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avertissement
        fields = [
            "id_avertissement", "nombre_avertissement", "id_membre", "id_presence"
        ]
        read_only_fields = ["id_avertissement", "nombre_avertissement"]
