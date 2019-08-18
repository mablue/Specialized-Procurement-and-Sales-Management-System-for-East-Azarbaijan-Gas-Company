from django.contrib import admin

# Register your models here.
from tasfie.models import Tasfie


class TasfieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'taghaza',
        'bank',
        'shomare',
        'tarikh',
        'mablagh',
        'noe',
    )

    list_filter = (
        'id',
        'taghaza',
        'shomare',
        'tarikh',
        'mablagh',
        'noe',
    )
    search_fields = (
        'id',
        'taghaza',
        'shomare',
        'tarikh',
        'mablagh',
        'noe',

    )


admin.site.register(Tasfie, TasfieAdmin)
