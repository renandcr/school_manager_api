from django.urls import path
from . import views

urlpatterns = [
    path('school/<school_id>/', views.SchoolView.as_view()),
    path('school/', views.SchoolCreateGetView.as_view())
]