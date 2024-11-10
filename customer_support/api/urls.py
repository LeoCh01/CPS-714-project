from django.urls import path
from . import views

urlpatterns = [
    path('user', views.get_User),
    path('user/create', views.set_User),
]
