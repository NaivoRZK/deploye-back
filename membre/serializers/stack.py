from rest_framework import serializers
from .models.stack import Stack  # recuperation de modele sur agenda.py


class StackSociauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = [
            "id_stack", "nom_stack", "hard", "soft"
        ]
        read_only_fields = ["id_stack", "nom_stack"]
