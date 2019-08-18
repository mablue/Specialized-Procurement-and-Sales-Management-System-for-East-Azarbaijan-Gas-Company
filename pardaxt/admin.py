from django.contrib import admin

# Register your models here.

from pardaxt.models import Pardaxt


class PardaxtAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fish',
        'hesab',
        'name_bank',
        'elame_vajh',
        # 'getSherkat',
        'factor',


    )
    list_filter = (
        # 'id',
        # 'fish',
        # 'hesab',
        'name_bank',
        'elame_vajh',
        'factor__shomare',
        # 'tarikh',

    )
    search_fields = (
        'id',
        'fish',
        'hesab',
        'name_bank',
        'elame_vajh',
        'factor__shomare',
        # 'tarikh',

    )


admin.site.register(Pardaxt, PardaxtAdmin)
