from . import views
from django.urls import path

urlpatterns = [
    path("school", views.SchoolView.as_view()),
    path("school/<school_id>", views.SchoolView.as_view())
]