from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:pk>/', views.get_User),
    path('user/create', views.set_User),
    path('tickets/<int:pk>/', views.get_Ticket),
    path('tickets/', views.get_all_Tickets),
    path('tickets/create', views.set_Ticket),
]
