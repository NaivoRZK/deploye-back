# /home/odoo-5/techzara-backend/formation/views/formateur.py

from rest_framework import generics
from formation.models.formateur import Formateur
from formation.serializers.formateur import FormateurSerializer

#Ajouter un formateur
class FormateurCreateAPIView(generics.CreateAPIView):
    queryset = Formateur.objects.all()
    serializer_class = FormateurSerializer
