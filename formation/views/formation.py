from rest_framework import generics, status
from rest_framework.response import Response
from formation.models.formation import Formation
from formation.serializers.formation import FormationSerializer

# ====================================================
# Création de formation avec réponse personnalisée
# ====================================================
class FormationCreateAPIView(generics.CreateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            formation = serializer.save()
            return Response(
                {
                    "message": "Formation créée avec succès !",
                    "formation": FormationSerializer(formation).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "Erreur lors de la création de la formation",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

# ====================================================
# Liste des formations avec réponse personnalisée
# ====================================================
class FormationListAPIView(generics.ListAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer

    def list(self, request, *args, **kwargs):
        formations = self.get_queryset()
        serializer = self.get_serializer(formations, many=True)
        return Response(
            {
                "message": f"{formations.count()} formations trouvées",
                "formations": serializer.data
            },
            status=status.HTTP_200_OK
        )
