from django.contrib import admin

from .models import Scoala, ClaseScoala, Profesori, Elevi, ParinteElev

class ScoalaAdmin(admin.ModelAdmin):
    list_display = ("nume_scoala", )
    list_filter = ("nume_scoala","judet")
    search_fields = ("nume_scoala", "judet")
    
class ClaseAdmin(admin.ModelAdmin):
    list_display = ( "nume_clasa")
    list_filter = ("nume_clasa" )
    search_fields = ("nume_clasa", "promotia")
    
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nume_profesor", "materie")
    search_fields = ("nume_profesor", "materie",)
    
class ElevAdmin(admin.ModelAdmin):
    list_display = ("nume_elev", "clasa")
    list_filter = ("clasa", "nume_elev" )
    search_fields = ("clasa", "nume_elev",)

# Register your models here.
#admin.site.register(Scoala, ScoalaAdmin)
#admin.site.register(ClaseScoala, ClaseAdmin)
#admin.site.register(Profesori, ProfesorAdmin)
admin.site.register(Elevi, ElevAdmin)
#admin.site.register(ParinteElev)