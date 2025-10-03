from rest_framework import serializers
from .models.badge import Badge  # recuperation de modele sur agenda.py


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = [
            "id_badge", "id_membre", "qr_code", "date_generation"
        ]
        read_only_fields = ["id_archive", "date_generation"]
