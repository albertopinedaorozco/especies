from django.contrib import admin

from .models import (
    Proyecto,
    Ecorregion,
    RegistroBiologico
)

admin.site.register(Proyecto)
admin.site.register(Ecorregion)
admin.site.register(RegistroBiologico)

