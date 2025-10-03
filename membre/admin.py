from django.contrib import admin
from .models.archive import Archive
from .models.avertissement import Avertissement
from .models.badge import Badge
from .models.demandeFormation import DemandeFormation
from .models.membre import Membre
from .models.presence import Presence
from .models.reseauSociaux import ReseauSociaux
from .models.stack import Stack
from .models.statusCompte import StatusCompte

# Register your models here.
admin.site.register(Archive)
admin.site.register(Avertissement)
admin.site.register(Badge)
admin.site.register(DemandeFormation)
admin.site.register(Membre)
admin.site.register(Presence)
admin.site.register(ReseauSociaux)
admin.site.register(Stack)
admin.site.register(StatusCompte)