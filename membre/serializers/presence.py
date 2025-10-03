from rest_framework import serializers
from .models.presence import Presence  # recuperation de modele sur agenda.py


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = [
            "id_presence", "presence", "activite", "date",
            "heure", "id_formation"
        ]
        read_only_fields = ["id_presence", "presence"]
