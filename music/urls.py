from django.urls import path
from . import views

urlpatterns = [
    path(route='about/', view=views.about)
]