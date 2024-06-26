from django.contrib import admin
from .models import *
import logging

logger = logging.getLogger(__name__)

class EventInline(admin.TabularInline):
    model = Event
    extra = 3
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Filtrar els jugadors dels dos equips del partit actual
        if db_field.name == "jugador" or db_field.name == "jugador2":
            try:
                # Obtenim l'instance del Partit directament de kwargs
                partit = kwargs.get('instance').partit
                kwargs["queryset"] = Jugador.objects.filter(equip__in=[partit.local, partit.visitant])
            except AttributeError:
                #logger.error(f"SNo s'ha trobat el partit o el jugador: {partit}")
                pass  # No fer res si no es pot obtenir l'instance del Partit
        elif db_field.name == "equip":
            try:
                partit = kwargs.get('instance').partit
                kwargs["queryset"] = Equip.objects.filter(pk__in=[partit.local.pk, partit.visitant.pk])
            except AttributeError:
                pass  # No fer res si no es pot obtenir l'instance del Partit
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PartitAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Local", {"fields": ["local"]}),
        ("Visitant", {"fields": ["visitant"]}),
        ("Lliga", {"fields": ["lliga"]}),
        ("Inici", {"fields": ["inici"]}),

    ]
    inlines = [EventInline]
    list_display = ["local","visitant","lliga","detalls", "inici"]
    list_filter = ["lliga"]
    search_fields = ["local__nom","visitant__nom"]
    # el camp personalitzat ("resultats" o recompte de gols)
    # el mostrem com a "readonly_field"
    readonly_fields = ["resultat",]
    def resultat(self,obj):
        gols_local = obj.gols_local()
        gols_visit = obj.gols_visitant()
        return "{} - {}".format(gols_local,gols_visit)
    

admin.site.register(Lliga)
admin.site.register(Equip)
admin.site.register(Jugador)
admin.site.register(Partit,PartitAdmin)
admin.site.register(Event)


