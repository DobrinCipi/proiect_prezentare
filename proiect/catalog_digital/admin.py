from django.contrib import admin

from .models import Scoala, ClaseScoala

class ScoalaAdmin(admin.ModelAdmin):
    list_display = ("nume_scoala", )
    list_filter = ("nume_scoala","judet")
    search_fields = ("nume_scoala", "judet")
    
class ClaseAdmin(admin.ModelAdmin):
    list_display = ("scoala", "nume_clasa")
    list_filter = ("scoala", )
    search_fields = ("scoala", "nume_clasa", "promotia")

# Register your models here.
admin.site.register(Scoala, ScoalaAdmin)
admin.site.register(ClaseScoala, ClaseAdmin)