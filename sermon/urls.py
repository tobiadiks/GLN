from django.urls import path
from .views import Sermons, SingleSermon
urlpatterns = [
      path('sermon/', Sermons, name='sermon'),
      path('sermon/<slug:slug>/', SingleSermon, name = 'single-sermon'),
]