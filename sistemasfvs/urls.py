from django.urls import path
from .views import home
from .views import my_logout, perfil
from .views import status_list
from .views import status_create
from .views import status_view
from .views import status_update
from .views import status_delete
from .views import fase_list
from .views import fase_create
from .views import fase_add
from .views import fase_sf_delete
from .views import fase_sf_update
from .views import fase_view
from .views import fase_update
from .views import fase_delete
from .views import sistema_list
from .views import sistema_create
from .views import sistema_view
from .views import sistema_update
from .views import sistema_delete
from .views import sistema_doctos
from .views import sistema_fases
from .views import documento_create
from .views import documento_update
from .views import documento_view
from .views import documento_delete
from .views import altera_foto


urlpatterns = [
    path('', home, name="home"),
    path('perfil', perfil, name="perfil"),
    path('altera_foto', altera_foto, name="altera_foto"),
    path('logout/', my_logout, name="logout"),
    path('status_list', status_list, name="status_list"),
    path('status_create', status_create, name="status_create"),
    path('status_view/<int:id>', status_view, name="status_view"),
    path('status_update/<int:id>', status_update, name="status_update"),
    path('status_delete/<int:id>', status_delete, name="status_delete"),

    path('fase_list', fase_list, name="fase_list"),
    path('fase_create', fase_create, name="fase_create"),

    path('fase_add/<int:id>', fase_add, name="fase_add"),
    path('fase_sf_delete/<int:id>', fase_sf_delete, name="fase_sf_delete"),
    path('fase_sf_update/<int:id>', fase_sf_update, name="fase_sf_update"),

    path('fase_view/<int:id>', fase_view, name="fase_view"),
    path('fase_update/<int:id>', fase_update, name="fase_update"),
    path('fase_delete/<int:id>', fase_delete, name="fase_delete"),

    path('sistema_list', sistema_list, name="sistema_list"),
    path('sistema_create', sistema_create, name="sistema_create"),
    path('sistema_view/<int:id>', sistema_view, name="sistema_view"),
    path('sistema_update/<int:id>', sistema_update, name="sistema_update"),
    path('sistema_delete/<int:id>', sistema_delete, name="sistema_delete"),
    path('sistema_doctos/<int:id>', sistema_doctos, name="sistema_doctos"),
    path('sistema_fases/<int:id>', sistema_fases, name="sistema_fases"),

    path('documento_create/<int:id>', documento_create, name="documento_create"),
    path('documento_view/<int:sis_id>/<int:id>', documento_view, name="documento_view"),
    path('documento_update/<int:sis_id>/<int:id>', documento_update, name="documento_update"),
    path('documento_delete/<int:sis_id>/<int:id>', documento_delete, name="documento_delete")
]