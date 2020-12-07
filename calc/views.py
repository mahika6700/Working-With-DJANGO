from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html",{'name':'mahika'})  

def add(request):

     x= int(request.POST["n1"])
     y= int(request.POST["n2"])
     res=x+y
     return render(request, "result.html", {'result': res})
     
    
   
