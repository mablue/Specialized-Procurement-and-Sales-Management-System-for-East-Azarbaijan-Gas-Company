import locale

import xadmin
from django.utils.safestring import mark_safe

from aghlam.models import Aghlam
from factor.models import Factor
from salemali.models import Salemali


class FactorAdmin(object):
    list_display = (
        'id',
        'taghaza',
        'shomare',
        'tarikh',
        'arzeshe_afzude',
        'mablaghe_koll_splited',
        'linkha',
    )

    list_filter = (
        'id',
        'taghaza',
        'shomare',
        'tarikh',
        # 'arzeshe_afzude',
        # 'mablaghe_koll',
        # 'linkha',
    )
    search_fields = (
        'id',
        # 'taghaza',
        'shomare',
        'tarikh',
        # 'arzeshe_afzude',
        # 'mablaghe_koll_splited',
        # 'linkha',
    )

    def linkha(self, obj):
        # link = reverse("admin:foo_bar_change", args=[obj.bar.id])
        # return u'<a href="%s">%s</a>' % (link, obj.bar.id)
        return mark_safe(
            u'<a href="%s">%s</a>' % (
                "/aghlam/aghlam/?factor__id__exact=" + str(obj.id)
                , "اقلام")

        )

    linkha.short_description = "لینک ها"

    def arzeshe_afzude(self, qq):
        try:
            if qq.arzeshe_afzude:
                i = Salemali.objects.filter(sal=qq.tarikh.year).values_list("arzeshe_afzude")[0][0]
                return (i + 100) / 100
            else:
                return 1
        except:
            return 1

    arzeshe_afzude.short_description = "ارزش افزوده"

    def mablaghe_koll(self, qq):
        maghadir = ()
        for i in Aghlam.objects.filter(factor_id=qq.id).values_list("meghdar"):
            maghadir += i
        mabalegh = ()
        for i in Aghlam.objects.filter(factor_id=qq.id).values_list("mablagh"):
            mabalegh += i
        total = [a * b for a, b in zip(mabalegh, maghadir)]
        na = self.arzeshe_afzude(qq)
        return round(sum(total) * na)

    def mablaghe_koll_splited(self, qq):
        locale.setlocale(locale.LC_ALL, 'fa')
        return locale.currency(self.mablaghe_koll(qq), grouping=True)

    mablaghe_koll_splited.short_description = "مبلغ کل"


xadmin.site.register(Factor, FactorAdmin)
