from django.shortcuts import render
# importing models
from App.models import *
# importing length function
from django.db.models.functions import Length

# Create your views here.
def show_topics(request):
    # using all method which show all data
    topics=Topic.objects.all()
    # using filter method which show data of satisfied condition
    topics=Topic.objects.filter(topic_name='Cricket')
    # topics=Topic.objects.get(topic_name='Cricket')
    d={'topics':topics}
    return render(request,'show_topics.html',d)

def show_webpages(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(name='A')
    # webpages=Webpage.objects.get(name='A')
    # using exclude method which show data of unsatisfied condition
    webpages=Webpage.objects.exclude(name='A')
    # based on ASCII value arranging in ascending using order_by
    webpages=Webpage.objects.all().order_by('topic_name')
    # based on ASCII value arranging in descending using order_by
    webpages=Webpage.objects.all().order_by('-name')
    # based on length of cloumn  arranging in ascending using order_by
    webpages=Webpage.objects.all().order_by(Length('topic_name'))
    # based on length of column arranging in descending using order_by
    webpages=Webpage.objects.all().order_by(Length('url').desc())
    # getting particular rows data
    webpages=Webpage.objects.all()[::-1]
    webpages=Webpage.objects.all()[:3:]
    webpages=Webpage.objects.all()[4:9:]
    # webpages=Webpage.objects.all()[8:2:-1]
    
    d={'webpages':webpages}
    return render(request,'show_webpages.html',d)

def show_records(request):
    records=AccessRecord.objects.all()
    records=AccessRecord.objects.filter(author='A')
    # records=AccessRecord.objects.get(author='A')
    d={'records':records}
    return render(request,'show_records.html',d)