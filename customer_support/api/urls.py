from django.urls import path
from . import views


urlpatterns = [
    path('user/<int:pk>/', views.get_User),
    path('user/', views.get_all_Users),
    path('user/create', views.set_User),
    path('tickets/<int:pk>/', views.get_Ticket),
    path('tickets/', views.get_all_Tickets),
    path('tickets/create', views.set_Ticket),
    path('chatlogs/<int:pk>/', views.get_Chat_Log),
    path('chatlogs/', views.get_all_Chat_Logs),
    path('chatlogs/create', views.set_Chat_Log),
    path('roles/<int:pk>/', views.get_Role),
    path('roles/', views.get_all_Roles),
    path('roles/create', views.set_Role),
]
