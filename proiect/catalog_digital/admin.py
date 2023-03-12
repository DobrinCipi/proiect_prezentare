from django.contrib import admin

from .models import Scoala

class ScoalaAdmin(admin.ModelAdmin):
    list_display = ("nume_scoala", )
    list_filter = ("nume_scoala","judet")
    search_fields = ("nume_scoala", "judet")
    

# Register your models here.
admin.site.register(Scoala, ScoalaAdmin)