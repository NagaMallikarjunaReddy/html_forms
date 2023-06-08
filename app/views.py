from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['ps']
        return HttpResponse('Topic Data inserted successfully')
    
    return render(request,'t1.html')