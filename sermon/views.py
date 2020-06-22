from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Sermon
from glife.models import Service

def Sermons(request):
	sermon_list = Sermon.objects.all()
	paginator = Paginator(sermon_list, 3)
	page = request.GET.get('page', 1)
	sermon = paginator.get_page(page)
	service= Service.objects.all
	
	
	return render(request, 'sermons.html', {'sermon' : sermon, 'service' : service ,})
	
def SingleSermon(request, slug):
	
	sermon = Sermon.objects.get(slug = slug)
	recent_sermon = Sermon.objects.all()[:4]
	return render(request, 'sermon-single.html', {'sermon':sermon,'recent_sermon':recent_sermon ,})
# Create your views here.
