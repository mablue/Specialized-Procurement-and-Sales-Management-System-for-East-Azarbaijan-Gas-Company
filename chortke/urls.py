"""chortke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
# from django.urls import path
from django.urls import path, include

from taghaza import views

from django.utils.translation import ugettext_lazy as _




# # -*- coding: utf-8 -*-
# import xadmin
# xadmin.autodiscover()

# # version模块自动注册需要版本控制的 Model
# from xadmin.plugins import xversion
# xversion.register_models()


urlpatterns = [
                url(r'^', admin.site.urls),
                # path('/', admin.site.urls),
                path('reports', views.report, name='report'),
                # url(r'xadmin/', xadmin.site.urls),
                url(r'^_nested_admin/', include('nested_admin.urls')),
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Change admin site title
admin.site.site_header = _("سیستم مدیریت خرید‌های داخلی امور‌ تدارکات و عملیات شرکت گاز استان آذربایجان شرقی")
admin.site.site_title = _("سیستم مدیریت خرید‌های داخلی امور‌ تدارکات و عملیات شرکت گاز استان آذربایجان شرقی")