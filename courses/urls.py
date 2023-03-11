from django.urls import path
from . import views

urlpatterns = [
    path('course/instructor/<course_id>/<user_email>', views.CourseAddAndRemoveInstructorView.as_view()),
    path('course/student/<course_id>/<student_email>', views.CourseAddAndRemoveStudentView.as_view()),
    path('course/create/<school_id>', views.CourseCreateGetView.as_view()),
    path('course/get/<school_id>', views.CourseCreateGetView.as_view()),
    path('course/<course_id>', views.CourseView.as_view())
]