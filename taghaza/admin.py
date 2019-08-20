import locale

# import nested_admin
from django.contrib import admin
from django.shortcuts import render_to_response
from django.urls import reverse
from django.utils.safestring import mark_safe
from rangefilter.filter import DateRangeFilter
import re
from aghlam.models import Aghlam
from factor.models import Factor
from resid.models import Resid
from tasfie.models import Tasfie
from salemali.models import Salemali
from taghaza import views
from taghaza.models import Taghaza
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from import_export import resources
from import_export.fields import Field


class TaghazaResource(resources.ModelResource):
    splited_price = Field(column_name='مبلغ کل')
    splite_price = Field(column_name='مبلغ تفکیک')
    type = Field(column_name='نوع')
    id = Field(column_name='id',attribute='id')
    shomare = Field(column_name='شماره تقاضا',attribute='shomare')
    tarikh = Field(column_name='تاریخ تقاضا',attribute='tarikh')
    sharh = Field(column_name='شرح',attribute='sharh')
    baravord = Field(column_name='مبلغ براورد اولیه',attribute='baravord')
    vahed = Field(column_name='واحد تقاضا کننده',attribute='vahed')
    image = Field(column_name='فرم تقاضا',attribute='image')
    factors = Field(column_name='فاکتورها')
    aghlam = Field(column_name='فاکتورها')
    fields = (id, shomare, tarikh, sharh, vahed, splite_price, type, splited_price, aghlam, factors, image)

    class Meta:
        model = Taghaza
        # widgets = {
        #     'published': {'format': '%d.%m.%Y'},
        #     }
    def dehydrate_splited_price(self, taghaza):
        total = taghaza.price()
        return '{:0,.0f}'.format(total)
        # locale.setlocale(locale.LC_ALL, 'fa')
        # return locale.currency(total, grouping=True)
    def dehydrate_factors(self,taghaza):
        return [str(i)+"\n" for i in taghaza.factor_set.all()]
    def dehydrate_aghlam(self,taghaza):
        return [str(i)+"\n" for i in taghaza.aghlam_set.all()]
    
    def dehydrate_splite_price(self, taghaza):
        try:
            i = Salemali.objects.filter(sal=taghaza.tarikh.year).values_list("nerkhe_tafkik")[0][0]
            # return round((i + 100) / 100) - 1 # نمیدونم چرا این کارو کردم؟
            # return '{:20,.0f}'.format(i)
            # return '{:20,.0f}'.format(str(i))
            return i+100-1 # ????????
        except:
            return 0

    def dehydrate_type(self, taghaza):
        nt = self.dehydrate_splite_price(taghaza)
        nm = None
        if self.fields == 0:
            return "---"
        elif taghaza.price() <= nt:
            return "جزئی"
        else:
            return "متوسط"

class AghlamInline(admin.TabularInline):
    extra = 0

    model = Aghlam
    # sortable_field_name = "factor"
    fieldsets = (
        (None, {'fields': (
            'kala',
            # 'taghaza',
            'meghdar',
        )}),
    )
class FactorInline(admin.TabularInline):
    extra = 0
    model = Factor
    fieldsets = (
        (None, {'fields': (('shomare','tarikh','arzeshe_afzude'),'image')}),
    )
    
class ResidInline(admin.TabularInline):
    extra = 0
    model = Resid

class TasfieInline(admin.TabularInline):
    extra =0
    model = Tasfie


class TaghazaAdmin(ImportExportModelAdmin,admin.ModelAdmin,):

    extra = 0
    resource_class = TaghazaResource
    inlines = [AghlamInline,FactorInline,ResidInline,TasfieInline]



    # hide delete Action
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if request.user.username[0].upper() != 'J':
    #         if 'delete_selected' in actions:
    #             del actions['delete_selected']
    #     return actions

    # for Export As xls
    def get_export_formats(self):
        """
        Returns available export formats.
        """
        formats = ( 
            base_formats.XLS,
            # base_formats.CSV,
            # base_formats.XLSX,
            # base_formats.TSV,
            # base_formats.ODS,
            # base_formats.JSON,
            # base_formats.YAML,
            # base_formats.HTML,  
        )
        return [f for f in formats if f().can_export()]


        

    fieldsets = (
        # ('اطلاعات اصلی', {'fields':(tuple([]))}),
        ('ورود اطلاعات تقاضا', {
            'classes': ('wide', 'extrapretty'),

            'fields': ( ( 'shomare', 'tarikh' ),( 'sharh','baravord' ),( 'vahed','image' ) )
        }),
 
        ('بیشتر', {
            'classes': ('collapse',),
            'fields': (
                'splited_price',
                'image_tag',     
                'type',
                'count',  
                'linkha',                           

            ),
        }),    
        


    )

    # model = Taghaza
    # sortable_field_name = "position"
    actions = ['report']
    list_per_page = 100
    list_display = (
        'id',
        'shomare',
        'vahed',
        'sharh',
        'splite_price',
        'type',
        'count',
        'tarikh',
        'baravord',
        'splited_price',
        'linkha',
        'image_tag',
    )
    readonly_fields = (
        'image_tag',
        'linkha',
        'splited_price',
        'splite_price',
        'type',
        'count',

    )
    list_filter = (
        'vahed',
        # 'tarikh',
        # ('tarikh', JDateFieldListFilter),
        ('tarikh', DateRangeFilter),

    )
    search_fields = (
        'id',
        'shomare',
        'vahed',
        'sharh',
        'tarikh',
    )

    def linkha(self, obj):
        # link = reverse("admin:foo_bar_change", args=[obj.bar.id])
        # return u'<a href="%s">%s</a>' % (link, obj.bar.id)

        # sefaresh_url = reverse('admin:sefaresh_sefaresh_changelist')
        factor_url = reverse('admin:factor_factor_changelist')
        # pardakht_url = reverse('admin:pardaxt_pardaxt_changelist')
        aghlam_url = reverse('admin:aghlam_aghlam_changelist')
        resid_url = reverse('admin:resid_resid_changelist')
        tasfie_url = reverse('admin:tasfie_tasfie_changelist')

        return mark_safe(
            # '<a href="{}?taghaza__id__exact={}">{}</a>'
            '<a href="{}?taghaza__id__exact={}">{}</a>'
            # ' , <a href="{}?taghaza__id__exact={}">{}</a>'
            # ' , <a href="{}?taghaza__id__exact={}">{}</a>'
            '،<a href="{}?taghaza__id__exact={}">{}</a>'
            '،<a href="{}?taghaza__id__exact={}">{}</a>'
                .format(
                # sefaresh_url,
                # obj.id,
                # "سفارش",
                factor_url,
                obj.id,
                "فاکتور",
                # pardakht_url,
                # obj.id,
                # "پرداخت",
                # aghlam_url,
                # obj.id,
                # "اقلام",
                resid_url,
                obj.id,
                "رسید",
                tasfie_url,
                obj.id,
                "تسویه",
            )
        )

    linkha.short_description = "لینک ها"

    def splited_price(self, request):
        total = request.price()
        return '{:0,.0f}'.format(total)
        # locale.setlocale(locale.LC_ALL, 'fa')
        # return locale.currency(total, grouping=True)

    splited_price.short_description = "مبلغ کل"

    def splite_price(self, request):
        try:
            i = Salemali.objects.filter(sal=request.tarikh.year).values_list("nerkhe_tafkik")[0][0]
            return i
        except:
            return 0

    splite_price.short_description = "نرخ تفکیک"

    def type(self, request):
        nt = self.splite_price(request)
        nm = None
        if self.fields == 0:
            return "---"
        elif request.price() <= nt:
            return "جزئی"
        else:
            return "متوسط"

    type.short_description = "نوع معامله"

    def report(self, request, queryset):
        views.report(request)
        return render_to_response('reports/TaghazaReport.html', {'taghazaha': queryset})

    report.short_description = "تهیه گذارش قابل چاپ"



admin.site.register(Taghaza, TaghazaAdmin)



# def maghadir(qq):
#     fields = (
#         'shomare',
#         'sharh',
#         'splite_price',
#         'type',
#         'count',
#         'tarikh',
#         'vahed',
#         'splited_price',

#         'linkha',
#     )

# maghadir = ()
# qs = Aghlam.objects.filter(taghaza_id=qq.id).values_list("meghdar")
# # qs = Taghaza.aghlam_set.all().values_list("meghdar")

# for i in qs:
#     maghadir += i
# return maghadir
