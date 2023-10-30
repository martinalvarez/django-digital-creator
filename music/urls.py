from django.urls import path
from . import views

urlpatterns = [
    path(route='about/', view=views.about),
    path(route='guide/', view=views.guide),
    path(route='guide/albums/', view=views.get_guide_album),
]