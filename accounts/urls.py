from django.urls import path
from . import views

urlpatterns = [
    path('user/create/<school_id>', views.UserCreateView.as_view()),
    path('user/get/<school_id>', views.UserGetView.as_view()),
    path('user/<user_id>', views.UserView.as_view())
]
