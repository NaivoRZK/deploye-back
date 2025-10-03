from rest_framework import serializers
from formation.models.formateur import Formateur

class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = [
            "id_formateur",
            "nom_formateur",
            "prenom_formateur",
            "id_membre",
        ]
        read_only_fields = ["id_formateur"]

    id_membre = serializers.PrimaryKeyRelatedField(
        queryset=Formateur._meta.get_field("id_membre").related_model.objects.all(),
        required=False,
        allow_null=True
    )
