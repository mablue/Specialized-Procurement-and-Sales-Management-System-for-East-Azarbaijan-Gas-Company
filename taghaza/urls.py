from django.urls import path

from taghaza import views
# from taghaza.views import show_genres

urlpatterns = [
    path('', views.report),
]
