from rest_framework import serializers
from membre.models.archive import Archive  # recuperation de modele sur agenda.py


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = [
            "id_archive", "id_badge", "motif", "date_archivage"
        ]
        read_only_fields = ["id_archive", "motif"]
