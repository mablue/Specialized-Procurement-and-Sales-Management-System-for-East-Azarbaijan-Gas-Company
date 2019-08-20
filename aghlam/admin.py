
# from admin_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce

# Register your models here.
from aghlam.models import Aghlam


class AghlamAdmin(admin.ModelAdmin):


    # fieldsets = ((None, 
    #     {'fields': ((
    #             'taghaza',
    #             'kala',
    #             'sherkat',
    #             'mablagh',
    #             'meghdar',
    #             'external',
    #            ),)
    #     }),)
    list_display = (
        'id',
        # 'taghaza',
        # 'factor',
        'kala',
        'external',
        'sherkat',
        'mablagh',
        'meghdar',
        'mablaghe_koll_splited',
        # 'kala',
        # 'sherkat',
    )
    list_totals = [
        ('mablagh', lambda field: Coalesce(Sum(field), 0)),
        ('meghdar', lambda field: Coalesce(Sum(field), 0)),
        ]

    list_filter = (
        'external',
        # 'factor',
        'kala',
        'sherkat',
        'mablagh',
        'meghdar',

    )
    # search_fields = (
    #     'id',
    #     'sherkat',
    #     'mablagh',
    #     'meghdar',

    # )


admin.site.register(Aghlam, AghlamAdmin)
