from django.urls import path
from formation.views.formation import FormationCreateAPIView, FormationListAPIView
from formation.views.formateur import FormateurCreateAPIView
from formation.views.agenda import AgendaCreateAPIView


urlpatterns = [
    # Formation
    path('formations/create/', FormationCreateAPIView.as_view(), name='formation-create'),

    # Formateur
    path('formateurs/create/', FormateurCreateAPIView.as_view(), name='formateur-create'),

    # Lister tous les formations existantes
    path('formations/', FormationListAPIView.as_view(), name='formation-list'),

    # Ajouter une formation à l’agenda
    path('agenda/create/', AgendaCreateAPIView.as_view(), name='agenda-create'),

]
