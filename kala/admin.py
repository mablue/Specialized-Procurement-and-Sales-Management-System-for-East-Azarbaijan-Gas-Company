from django.contrib import admin

# Register your models here.
from kala.models import Kala

from aghlam.models import Aghlam
class aghlamAdmin (admin.TabularInline):
    model = Aghlam
    extra=0
    # inlines = [aghlamAdmin,]





class KalaAdmin(admin.ModelAdmin):
    inlines = [aghlamAdmin,]
    list_display = (
        'id',
        # 'noe',
        'sharh',
        # 'abead',
        # 'shekl',
        # 'rang',
        # 'jens',
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
