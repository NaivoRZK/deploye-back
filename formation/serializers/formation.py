from rest_framework import serializers
from formation.models.formation import Formation  #recuperation de modele dans Formation.py


class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = [
            "id_formation", "title", "description",
            "date_formation","duree_formation","intervenant",
            "id_partner", "id_formateur", "id_membre"
        ]
        read_only_fields = ["id_formation"]

    def validate(self, data):
        # S’assurer que les clés étrangères manquantes n’empêchent pas la création
        data.setdefault("id_partner", None)
        data.setdefault("id_formateur", None)
        data.setdefault("id_membre", None)
        return data
