from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("all/", views.printAll, name="printAll"),
    path("gte/", views.filtergte, name="gte")
]