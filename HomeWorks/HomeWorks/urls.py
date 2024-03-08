from django.urls import path, include

urlpatterns = [
    path('weekdays/', include('weekdays.urls')),
    
]