from django.shortcuts import render
from App.models import *
# Create your views here.
def show_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'show_topics.html',d)

def show_webpages(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'show_webpages.html',d)

def show_records(request):
    records=AccessRecord.objects.all()
    d={'records':records}
    return render(request,'show_records.html',d)