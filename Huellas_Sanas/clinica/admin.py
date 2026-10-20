from django.contrib import admin
from .models import Cita, Mascota


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'nombre_dueno')
    search_fields = ('nombre', 'nombre_dueno', 'especie', 'raza')
    list_per_page = 25


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'mascota', 'motivo_consulta', 'estado')
    list_filter = ('fecha', 'estado')
    search_fields = ('mascota__nombre', 'mascota__nombre_dueno', 'motivo_consulta')
    date_hierarchy = 'fecha'
    ordering = ('fecha', 'hora')
    list_per_page = 25
