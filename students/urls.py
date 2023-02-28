from django.urls import path
from . import views

urlpatterns = [
    path('student/create/<school_id>', views.StudentCreateGetView.as_view()),
    path('student/get/<school_id>', views.StudentCreateGetView.as_view()),
    path('student/<student_id>', views.StudentView.as_view()),
]