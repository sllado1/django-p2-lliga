from django.urls import path

from . import views

app_name="lliga"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/classificacio/", views.classificacio, name="classificacio"),
    path("<int:pk>/partits/", views.partits, name="partits"),
]