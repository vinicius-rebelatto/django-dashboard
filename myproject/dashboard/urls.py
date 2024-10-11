#dashboard/urls

from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.my_view,),
]