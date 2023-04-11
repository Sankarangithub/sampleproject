from django.shortcuts import render,redirect
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def addDestination(request):
    return render(request,"addDestination.html")

def viewdestination(request):
    data=Destinations.objects.all()
    return render(request,"viewdestination.html",{'data':data})

def getdata(request):
    if request.method=="POST":
        destname=request.POST.get("destinationname")
        destdescription=request.POST.get("destinationdescription")
        destprize=request.POST.get("destinationprize")
        destimage=request.FILES["destinationimage"]
        data=Destinations(destinationName=destname,destinationDescription=destdescription,destinationPrize=destprize,destinationImage=destimage)
        data.save()
        return redirect("viewdestination")
    
def edit(request,id):
    data=Destinations.objects.filter(id=id)
    return render(request,"edit.html",{'data':data})

def update(request,id):
    if request.method=="POST":
        destname=request.POST.get("destinationname")
        destdescription=request.POST.get("destinationdescription")
        destprize=request.POST.get("destinationprize")
        try:
            img=request.FILES['destinationimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Destinations.objects.get(id=id).destinationImage
        Destinations.objects.filter(id=id).update(destinationName=destname,destinationDescription=destdescription,destinationPrize=destprize,destinationImage=file)
        return redirect("viewdestination")

def delete(request,id):
    Destinations.objects.filter(id=id).delete()
    return redirect("viewdestination")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")


def registerdata(request):
    if request.method=="POST":
        user_name=request.POST.get("username")
        user_password=request.POST.get("password")
        user_email=request.POST.get("email")
        user_phone=request.POST.get("phonenumber")
        details=Register(Username=user_name,Password=user_password,Email=user_email,Phone=user_phone)
        details.save()
        return redirect("login")

def logindata(request):
    if request.method=="POST":
        username2=request.POST['username']
        password2=request.POST['password']
        if Register.objects.filter(Username=username2,Password=password2).exists():
    
            return redirect("addDestination")
        else:
            return render(request,'login.html',{'msg':"invalid"})
    else:
        return redirect('login')
    
def index(request):
    return render(request,"index.html")










