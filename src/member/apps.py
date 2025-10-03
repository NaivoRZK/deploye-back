from django.apps import AppConfig

class MemberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.member'   # 👈 doit correspondre à INSTALLED_APPS
