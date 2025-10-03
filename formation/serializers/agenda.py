from rest_framework import serializers
from formation.models.agenda import Agenda

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ["id_agenda", "date_formation", "id_formation"]
        read_only_fields = ["id_agenda"]  # garder seulement id_agenda en lecture seule
