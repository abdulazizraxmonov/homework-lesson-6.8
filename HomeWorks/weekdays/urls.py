from django.urls import path
from weekdays import views

urlpatterns = [
    path('<str:language>/', views.weekdays_view, name='weekdays'),
    path('', views.weekdays_table_view, name='weekdays_table'),
    
]