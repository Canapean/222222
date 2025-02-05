from django.contrib import admin
from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_status', 'age')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(Cat, CatAdmin)
