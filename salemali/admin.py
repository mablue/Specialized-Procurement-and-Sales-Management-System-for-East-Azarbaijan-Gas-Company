from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.

from salemali.models import Salemali


class SalemaliAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sal',
        'arzeshe_afzude',
        'nerkhe_tafkik',
        # 'is_active',

    )
    list_filter = (
        'id',
        'sal',
        'arzeshe_afzude',
        'nerkhe_tafkik',
        # 'is_active',

    )
    search_fields = (
        'id',
        'sal',
        'arzeshe_afzude',
        'nerkhe_tafkik',
        # 'is_active',
    )


admin.site.register(Salemali, SalemaliAdmin)
