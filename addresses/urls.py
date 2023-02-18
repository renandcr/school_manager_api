from django.urls import path
from . import views

urlpatterns = [
    path('address/create/<student_id>', views.AddressCreateView.as_view()),
    path('address/<address_id>', views.AddressView.as_view())
]
