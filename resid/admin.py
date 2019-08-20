from django.contrib import admin
from django.shortcuts import render_to_response
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from resid import views
# Register your models here.
from resid.models import Resid


class ResidAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        # 'taghaza',
        'shomare',
        'tarikh',
    )
    list_filter = (
        'id',
        'shomare',
        # 'taghaza',
        # 'tarikh',
        ('tarikh', DateRangeFilter),
    )
    search_fields = (
        'id',
        # 'taghaza',
        'tarikh',
    )

    def get_actions(self, request):
            actions = super().get_actions(request)
            # if request.user.username[0].upper() != 'J':
            #     if 'delete_selected' in actions:
            del actions['delete_selected']
            return actions
    actions = ['report']
    def report(self, request, queryset):
            views.report(request)
            return render_to_response('reports/ResidReport.html', {'residha': queryset})
    
    report.short_description = "تهیه گذارش قابل چاپ"
    
admin.site.register(Resid, ResidAdmin)
