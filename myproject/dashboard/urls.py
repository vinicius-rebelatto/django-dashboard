#dashboard/urls

from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_view,),
    path("articles/<int:year>/", views.year_archive),
    path("tasks/", views.create_task)
]