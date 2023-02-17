from django.urls import path
from . import views

urlpatterns = [
    path('user/create/<school_id>', views.UserCreateView.as_view()),
    path('user/<school_id>/<user_id>', views.UserView.as_view()),
    path('user/<school_id>', views.UserView.as_view())
]
