from rest_framework import serializers
from .models.statusCompte import StatusCompte  # recuperation de modele sur agenda.py


class StatusCompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCompte
        fields = [
            "id_statuscompte", "id_membre", "status"
        ]
        read_only_fields = ["id_statuscompte", "status"]
