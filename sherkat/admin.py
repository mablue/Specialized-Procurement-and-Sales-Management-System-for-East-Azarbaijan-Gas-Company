from django.contrib import admin

# Register your models here.
from sherkat.models import Sherkat


class SherkatAdmin(admin.ModelAdmin):
    list_display = (
        'nam',
        'tel',
        'mob',
    )
    # list_filter = (
    #     # 'id',
    #     'nam',
    #     'tel',
    #     'mob',
    # )
    search_fields = (
        'id',
        'nam',
        'tel',
        'mob',
    )


admin.site.register(Sherkat, SherkatAdmin)
