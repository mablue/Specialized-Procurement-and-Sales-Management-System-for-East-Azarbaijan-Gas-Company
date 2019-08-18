import locale
import nested_admin
from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe
from rangefilter.filter import DateRangeFilter
from aghlam.models import Aghlam
from factor.models import Factor
from salemali.models import Salemali
from taghaza.models import Taghaza


# class AghlamInline(nested_admin.NestedStackedInline):
#     # extra = 2
#     model = Aghlam
#     # sortable_field_name = "factor"
#     fieldsets = (
#         (None, {'fields': (
#             'taghaza',
#             # 'factor',
#             'kala',
#             'sherkat',
#             'mablagh',
#             'meghdar',
#             'external',

#         )}),
#     )


# class FactorAdmin(nested_admin.NestedModelAdmin):
#     extra = 1
#     inlines = [AghlamInline]
class FactorAdmin(admin.ModelAdmin):

    # fieldsets = (
    #     (None, {'fields': (
    #                 'taghaza',
    #                 'shomare',
    #                 'tarikh',
    #                 'aghlam',
    #                 'image',
    #                 'arzeshe_afzude',
    #     )}),
    # )

    list_display = (
        # 'id',
        'taghaza',
        'shomare',
        'tarikh',
        'salemali',
        'arzeshe_afzude',
        'mablaghe_koll_splited',
        'linkha',
        'image_tag',
        # 'mablaghe_koll',

    )
    # all_fields = [f.name for f in Factor._meta.fields]
    # parent_fields = Taghaza.get_deferred_fields(Factor)

    # list_display = all_fields
    # read_only = parent_fields
    list_filter = (
        'id',
        'taghaza',
        'shomare',
        'tarikh',
        ('tarikh', DateRangeFilter),
        # 'salemali',

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
        for i in qq.aghlam.all().values_list("meghdar"):
            maghadir += i
        mabalegh = ()
        for i in qq.aghlam.all().values_list("mablagh"):
            mabalegh += i
        try:
            total = [a * b for a, b in zip(mabalegh, maghadir)]
        except:
            total = ()


        # mabalegh = Aghlam.objects.filter(factor_id=qq.id).values_list("mablagh")
        # maghadir = Aghlam.objects.filter(factor_id=qq.id).values_list("meghdar")
        # total = [a * b for a, b in zip(mabalegh, maghadir)]


        # mabalegh = qq.aghlam.all().values_list("mablagh")
        # maghadir = qq.aghlam.all().values_list("meghdar")

        # total = []
        # for a, b in zip(mabalegh, maghadir):
        #     try:
        #         total.append(a * b)
        #     except:
        #         pass

        na = self.arzeshe_afzude(qq)

        return round(sum(total) * na)

    def mablaghe_koll_splited(self, qq):
        return '{:0,.0f}'.format(self.mablaghe_koll(qq))
        # locale.setlocale(locale.LC_ALL, 'fa')
        # return locale.currency(self.mablaghe_koll(qq), grouping=True)

    mablaghe_koll_splited.short_description = "مبلغ کل"


admin.site.register(Factor, FactorAdmin)
