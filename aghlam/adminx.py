import xadmin
from aghlam.models import Aghlam
import locale


class AghlamAdmin(object):
    list_display = (
        'id',
        # 'taghaza',
        'factor',
        'kala',
        'sherkat',
        'mablagh',
        'meghdar',
        'mablaghe_koll_splited',
    )

    list_filter = (
        'id',
        # 'taghaza',
        'factor',
        'kala',
        'sherkat',
        'mablagh',
        'meghdar',

    )
    search_fields = (
        'id',
        # 'taghaza',
        'factor__shomare',
        # 'kala_nam',
        # 'sherkat_nam',
        'mablagh',
        'meghdar',
    )

    def mablaghe_koll(self,qq):
        return qq.meghdar * qq.mablagh

    def mablaghe_koll_splited(self, qq):
        locale.setlocale(locale.LC_ALL, 'fa')
        return locale.currency(self.mablaghe_koll(qq), grouping=True)

    mablaghe_koll_splited.short_description = "مبلغ کل"


xadmin.site.register(Aghlam, AghlamAdmin)
