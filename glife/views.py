from django.shortcuts import render
from .models import Home_Verse, Service, Leader, Gallery
from event.models import Event
from sermon.models import Sermon

def Home(request):
	verse = Home_Verse.objects.all
	service = Service.objects.all
	leader = Leader.objects.all
	event = Event.objects.all
	gallery = Gallery.objects.all
	latest_sermon = Sermon.objects.latest('date')
	#latest sermon query
 	latest_sermon_slug=latest_sermon.slug
	latest_sermon_title = latest_sermon.title
	latest_sermon_author = latest_sermon.author
	latest_sermon_date = latest_sermon.date
	latest_sermon_summary = latest_sermon.summary
	latest_sermon_videolink = latest_sermon.video_link
	latest_sermon_photo = latest_sermon.photo
	
	recent_sermon = Sermon.objects.all()[:3]
	
	gallery = Gallery.objects.all()[:4]
	return render(request, 'index.html', {'verse' : verse, 'service' : service , 'leader' : leader , 'event' : event , 'gallery' : gallery ,'latest_sermon_slug':latest_sermon_slug, 'latest_sermon_title' : latest_sermon_title , 'latest_sermon_author' : latest_sermon_author,
	'latest_sermon_date' : latest_sermon_date,
	'latest_sermon_summary' : latest_sermon_summary,
	'latest_sermon_videolink' : latest_sermon_videolink,
	'latest_sermon_photo': latest_sermon_photo ,'recent_sermon' : recent_sermon, 'gallery': gallery,})
	
	
def About(request):
	leader = Leader.objects.all
	service = Service.objects.all
	gallery = Gallery.objects.all()[:4]
	return render(request, 'about.html', {'service' : service , 'leader' : leader , 'gallery' : gallery ,})

def Contact(request):
	service = Service.objects.all
	verse = Home_Verse.objects.all
	return render(request, 'contact.html', {'service' : service , 'verse' : verse ,})
	
	
# Create your views here.
