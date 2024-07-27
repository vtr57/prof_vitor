from django.contrib import admin
from .models import NotasAula

class NotasAulaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status_publicado','caminho_html',)
    prepopulated_fields = {"slug": ("titulo",),}
    exclude = ('caminho_html',)
    
admin.site.register(NotasAula, NotasAulaAdmin)
