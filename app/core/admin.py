from django.contrib import admin

from app.core.models import Document


admin.site.site_header = 'EYAZIS Administration'


class DocumentAdmin(admin.ModelAdmin):
    search_fields = ('text',)


admin.site.register(Document, DocumentAdmin)
