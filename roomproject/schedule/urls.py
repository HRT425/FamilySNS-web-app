from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="schedule"),
    path("add/", views.add_event, name="add_event"),
    path("list/", views.get_events, name="get_events"),
]