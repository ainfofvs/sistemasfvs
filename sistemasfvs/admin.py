from django.contrib import admin
from .models import SistemaFase, Sistema, Status, Fase, Documento

# Register your models here.
admin.site.register(SistemaFase)
admin.site.register(Sistema)
admin.site.register(Fase)
admin.site.register(Status)
admin.site.register(Documento)
