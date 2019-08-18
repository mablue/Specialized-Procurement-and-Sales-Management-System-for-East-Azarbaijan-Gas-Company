import xadmin

# Register your models here.
from kala.models import Kala


class KalaAdmin(object):
    list_display = (
        'id',
        'sharh',
        'vahede_andazegiri',

    )
    list_filter = (
        'id',
        'sharh',
        'vahede_andazegiri',
    )
    search_fields = (
        'id',
        'sharh',
        'vahede_andazegiri',
    )


xadmin.site.register(Kala, KalaAdmin)
