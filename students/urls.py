from django.urls import path
from . import views

urlpatterns = [
    path('student/<school_id>', views.StudentView.as_view()),
    path('student/<school_id>/<student_id>', views.StudentView.as_view()),
    path('student/profile/<school_id>/<student_id>', views.StudentProfileView.as_view())
]