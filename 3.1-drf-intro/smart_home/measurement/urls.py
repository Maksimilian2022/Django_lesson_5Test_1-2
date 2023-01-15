from django.urls import path
from .views import Senser_control, Measurements

urlpatterns = [
    path('sensor/', Senser_control.as_view()),
    path('measurements/', Measurements.as_view())
]
