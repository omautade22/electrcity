from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import *
from .power import *
from django.contrib.sessions.models import Session
from django.forms import widgets

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
   # f = open('C:/Users/HP/Downloads/Code/cognatech/Stock/Stock_Market/Stock_Market/Stock_Market/household_power_consumption.txt', 'r')
   # file_contents = f.read()
   # f.close()
   # args = {'result': file_contents}
    return render(request, 'home.html')
def venderhome(request):
    return render(request, 'venderhome.html')
def adminhome(request):
    return render(request, 'adminhome.html')
def result(request):
    return render(request, 'result.html')
def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        print("email==", email)
        print("pass==", password)
        count = User.objects.filter(email=email,password=password).count()
        if count >0:
            #request.session['is_logged'] = True
            request.session['user_id'] = User.objects.values('id').filter(email=email,password=password)[0]['id']


            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'login.html')

def log(request):
    with open("D:/Electricity/household_power_consumption.txt", "r") as f:
        content = f.read()
    return render('home.html',  content=content )


def venderlogin(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        print("email==", email)
        print("pass==", password)
        count = User.objects.filter(email=email,password=password).count()
        if count >0:
            #request.session['is_logged'] = True
            request.session['user_id'] = User.objects.values('id').filter(email=email,password=password)[0]['id']
            return redirect('venderhome')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('venderlogin')
    return render(request, 'venderlogin.html')




def adminlogin(request):
    if request.POST:
        email = request.POST['email1']
        password = request.POST['password1']
        print("email==",email )
        print("pass==", password)



        e="admin@gmail.com"
        p="admin"
        if email == e and password == p:
             return redirect('adminhome')
        else:
             messages.error(request, 'Invalid email or password')
             return redirect('adminlogin')
    return render(request, 'adminlogin.html')


def signup(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj = User(username=username,email=email,password=password)
        obj.save()
        messages.success(request, 'You are registered successfully')
        return redirect('login')
    return render(request, 'signup.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):

    return render(request, 'about.html')
def search(request):
    SVM_result = ''

    if request.POST:
        post_request_allowed = ['search_text']
        r_no = []
        search_text = request.POST['search_text']
        print('prediction_list --- ', r_no)

    SVM_result= electricity_prediction(search_text)
    print("LSTM_result", SVM_result)



    return render(request, 'home.html',{'svm_result':SVM_result})
