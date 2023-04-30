from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,LoginForm,OrderForm
from django.contrib.auth import authenticate, login as do_login,logout
from .models import Users,Products,Orders
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
import datetime as dt
# Create your views here.
def index(request):
    products = Products.objects.filter().all()
    context = {"products":products,"user":request.user}
    return render(request,"main/index.html",context)

def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        checkExists = User.objects.filter(Q(username=username) | Q(email=email)).exists()
        if not checkExists:
            form = RegisterForm({"first_name":first_name,"last_name":last_name,"email":email,"username":username,"password":password})
            if form.is_valid():
                form.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    do_login(request, user)
                    return redirect("index")
            else:
                messages.error(request,"An error occured while signing you up.")
        else:
            messages.error(request,"A user already exists with these details.")
    form = RegisterForm()
    context = {"form":form}
    return render(request,"main/register.html",context)

def login(request):
    if request.user.is_authenticated:
            return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            do_login(request=request,user=user)
            return redirect("index")
        else:
            messages.error(request,"Invalid Login Details")
    form = LoginForm()
    context = {"form":form}
    return render(request,"main/login.html",context)

def user_logout(request):
    logout(request)
    return redirect("index")

@login_required(login_url="/login")
def order(request,id):
    product = Products.objects.filter(id=id).first()
    user = User.objects.filter(id=request.user.id).first()
    if request.method == "POST":
        date = dt.datetime.now()
        orderdata = {"product":product.id,"user":user.id,"address":request.POST["address"],"status":"Pending","added":date}
        print(orderdata)
        orderentry = OrderForm(orderdata)
        if orderentry.is_valid():
            orderentry.save()
            messages.success(request,"Order completed!")
    context = {"product":product,"user":user}
    return render(request,"main/order.html",context)