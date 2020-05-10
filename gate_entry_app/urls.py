from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name='people_list'),
    path('attendance_history/<int:pk>/', views.attendance_history, name='attendance_history'),
    path('entry_exit_simulation/', views.entry_exit_simulation, name='entry_exit_simulation')
]
