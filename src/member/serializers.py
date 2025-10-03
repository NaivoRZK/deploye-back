from rest_framework import serializers
from .models.model import User  # ou from .models import User si __init__.py importe déjà User
from .models.badge.model import badge
from .models.competence.model import competence 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id_member", "username", "email",
            "first_name", "last_name", "image",
            "inscription_date", "status", "badge_status",
            "address", "phone_number", "sexe", "role", "detail_status"
        ]
        read_only_fields = ["id_member", "inscription_date"]

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = badge
        fields = [
            "id_badge", #"id_member",
            "qr_code", "date_generation",
            "format_pdf"
        ]
        read_only_fields = ['id_badge','date_generation']

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = competence
        fields = [
            "id_competence", #"id_member",
            "qr_code", "date_generation",
            "format_pdf"
        ]
        read_only_fields = ['id_badge','date_generation']

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = badge
        fields = [
            "id_badge", #"id_member",
            "qr_code", "date_generation",
            "format_pdf"
        ]
        read_only_fields = ['id_badge','date_generation']
        
