from django.contrib import admin
from .models.agenda import Agenda
from .models.formateur import Formateur
from .models.formation import Formation
from .models.partner import Partner

# Register your models here.
admin.site.register(Agenda)
admin.site.register(Formateur)
admin.site.register(Formation)
admin.site.register(Partner)