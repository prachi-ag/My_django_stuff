from django.shortcuts import render
from django.http import HttpResponse
from app.models import Topic, AccessRecord, Webpage
# Create your views here.
def index(request):
    record = AccessRecord.objects.order_by('date')
    my_dir = {'include_me':record}
    return render(request,'index.html',context=my_dir)

def index1(request):
    return HttpResponse("Hello Kartikey")