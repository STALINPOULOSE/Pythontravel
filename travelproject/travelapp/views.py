from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Person


# Create your views here.

def demo(request):
    obj=Place.objects.all()
    obj1=Person.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})



# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})
# def contact(request):
#     return HttpResponse('hello am contact')