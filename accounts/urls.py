from django.urls import path
from . import views

urlpatterns = [
    path('user/<school_id>/<user_email>', views.UserAddSchoolView.as_view()),
    path('user/get/<school_id>/', views.UserGetView.as_view()),
    path('user/<user_id>', views.UserView.as_view()),
    path('user', views.UserCreateView.as_view()),
]
