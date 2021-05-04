from django.urls import path
from optifolio import views

urlpatterns = [
    path("", views.home, name="home"),
]