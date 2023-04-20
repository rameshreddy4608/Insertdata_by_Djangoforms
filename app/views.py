from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *
def insert_topicform(request):
    SOT=Studentform()
    d={'SOT':SOT}

    if request.method=='POST':
        STD=Studentform(request.POST)
        
        if STD.is_valid():
            topic_name=STD.cleaned_data['topic_name']
            TO=TOPICFORM.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()

            SQS=TOPICFORM.objects.all()
            d1={'SQS':SQS}
            return render(request,'display_topic.html',d1)
        
            return HttpResponse(str(STD.cleaned_data))



    return render(request,'insert_topicform.html',d)


def insert_webpageform(request):
    SOW=Studentformweb()
    d={'SOW':SOW}
    
    if request.method=='POST':
        SWD=Studentformweb(request.POST)

        if SWD.is_valid():
            topic_name=SWD.cleaned_data['topic_name']
            name=SWD.cleaned_data['name']
            url=SWD.cleaned_data['url']
            email=SWD.cleaned_data['email']
            TO=TOPICFORM.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            WO=WEBPAGESFORM.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
            WO.save()

            SQW=WEBPAGESFORM.objects.all()
            d1={'SQW':SQW}
            return render(request,'display_webpage.html',d1)
            
        

    return render(request,'insert_webpageform.html',d)


def insert_accessform(request):
    SOA=Studentformaccess()
    d={'SOA':SOA}

    if request.method=='POST':
        SAD=Studentformaccess(request.POST)

        if SAD.is_valid():
            name=SAD.cleaned_data['name']
            authour=SAD.cleaned_data['authour']
            date=SAD.cleaned_data['date']
            # topic_name=SAD.cleaned_data['topic_name']
            # url=SAD.cleaned_data['url']
            # email=SAD.cleaned_data['email']
            # TO=TOPICFORM.objects.get_or_create(topic_name=topic_name)[0]
            # TO.save()
            WO=WEBPAGESFORM.objects.get_or_create(name=name)[0]
            WO.save()
            AO=ACCESSRECORDSFORM.objects.get_or_create(name=WO,authour=authour,date=date)[0]
            AO.save()


            SQA=ACCESSRECORDSFORM.objects.all()
            d1={'SQA':SQA}
            return render(request,'display_accessform.html',d1)
    
    return render(request,'insert_accessform.html',d)