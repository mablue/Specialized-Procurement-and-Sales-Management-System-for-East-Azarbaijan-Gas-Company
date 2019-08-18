from django.contrib import admin

# Register your models here.
from kala.models import Kala


class KalaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sharh',
        'vahede_andazegiri',
        'mesc',

    )
    list_filter = (
        'id',
        'sharh',
        'vahede_andazegiri',
        'mesc',

    )
    search_fields = (
        'id',
        'sharh',
        'vahede_andazegiri',
        'mesc',

    )


admin.site.register(Kala, KalaAdmin)
