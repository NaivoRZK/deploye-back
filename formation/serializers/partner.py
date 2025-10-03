from rest_framework import serializers
from formation.models.partner import Partner  #recuperation de models dans le fichier Partner.py


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            "id_partner", "name", "Attribute",
        ]
        read_only_fields = ["id_partner", "name"]
