from django.urls import path
from .views import Events
urlpatterns = [
      path('event/', Events, name='event'),
]