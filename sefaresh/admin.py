from django.contrib import admin

# Register your models here.

from sefaresh.models import Sefaresh


class SefareshAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'taghaza',
        'kala',
        'meghdar',
    )
    list_filter = (
        # 'id',
        'taghaza',
        'kala',
        'meghdar',
    )
    search_fields = (
        'id',
        # 'taghaza__sharh',
        'kala__sharh',
        'meghdar',
    )


admin.site.register(Sefaresh, SefareshAdmin)
