from django.contrib import admin
from .models import Pais, Estado, Municipio, Bairro, Natureza, Escolaridade, Formacao
from .models import Entidade, Area, Atividade, Subatividade, Conselho, EntidadeSubatividade, EntidadeResponsavel
from .models import EntidadeUnidade, Areaproducao, Classeproducao, Linhaproducao, Formaproducao, EntidadeFormaproducao
from .models import EntidadeClasseproducao


# Register your models here.
admin.site.register(Pais)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Bairro)
admin.site.register(Natureza)
admin.site.register(Escolaridade)
admin.site.register(Formacao)
admin.site.register(Conselho)
admin.site.register(Entidade)
admin.site.register(Area)
admin.site.register(Atividade)
admin.site.register(Subatividade)
admin.site.register(EntidadeSubatividade)
admin.site.register(EntidadeResponsavel)
admin.site.register(EntidadeUnidade)
admin.site.register(Areaproducao)
admin.site.register(Classeproducao)
admin.site.register(Linhaproducao)
admin.site.register(Formaproducao)
admin.site.register(EntidadeFormaproducao)
admin.site.register(EntidadeClasseproducao)

