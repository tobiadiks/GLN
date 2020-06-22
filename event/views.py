from django.shortcuts import render
from .models import Event
from glife.models import Service
def Events(request):
	event = Event.objects.all
	service = Service.objects.all
	return render(request, 'events.html', {'event' : event , 'service' : service ,})
# Create your views here.
