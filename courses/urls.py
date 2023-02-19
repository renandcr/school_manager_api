from django.urls import path
from . import views

urlpatterns = [
    path('course/add/<course_id>/<student_id>', views.CourseAddStudentView.as_view()),
    path('course/create/<school_id>', views.CourseCreateGetView.as_view()),
    path('course/get/<school_id>', views.CourseCreateGetView.as_view()),
    path('course/<course_id>', views.CourseView.as_view())
]