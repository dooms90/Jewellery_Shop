from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

from .models import Contact
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        msg = request.POST.get("msg")
        c=Contact(name=name, email=email, phone=phone, msg=msg)
        c.save()
        return redirect('/contact')
    data=Contact.objects.all()
    return render(request,"contact.html",{'data': data})



def products(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,"products.html")

def loginView(request):
    if request.method== "POST":
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        user=User.objects.filter(username=userName,password=password)
        user = authenticate(username=userName, password=password)
        if user is not None:
            
            login(request,user)
            return redirect('/home')
        else:
            return render(request,"login.html",{"error":"Invalid username or password is incorrect"})
            
    return render(request,"login.html")

def signupView(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        userName = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if password==cpassword:
            user=User.objects.create_user(username=userName, email=email, password=password)
            user.first_name=firstName
            user.last_name=lastName
            user.save()
            return redirect('/login')
    return render(request,"signup.html")

def logoutView(request):
    logout(request)
    return redirect('/home')

