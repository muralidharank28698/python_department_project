# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from django.http import HttpResponse
from department.models import Register
from django.contrib import messages
# from .forms import Formregister

def index(request):
    return render(request,'index.html')


def department(request):
    # return HttpResponse("<h1>Hello Muralidharan...</h1>")
    # return render(request,'login.html')
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('email') and request.POST.get('password'):
            saverecord = Register()
            saverecord.uname = request.POST.get('uname')
            saverecord.email = request.POST.get('email')
            saverecord.password = request.POST.get('password')
            saverecord.save()
            messages.success(request,'record saved....')
            return render(request,'./department.html')
    else:
            return render(request,'./department.html')
        

def about(request):
    return render(request,'./about.html')


def ece(request):
    return render(request,'./ece.html')

def eee(request):
    return render(request,'./eee.html')

def cse(request):
    return render(request,'./cse.html')

def it(request):
    return render(request,'./it.html')

def me(request):
    return render(request,'./me.html')

def ce(request):
    return render(request,'./ce.html')

def mathematics(request):
    return render(request,'./mathematics.html')

def chemistry(request):
    return render(request,'./chemistry.html')

def csefaculty(request):
    return render(request,'./csefaculty.html')

def csesyllabus(request):
    return render(request,'./csesyllabus.html')

def csefacility(request):
    return render(request,'./csefacility.html')
# def insertrecord(request):
#     form = Formregister(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {'Formregister':Formregister}
#     return render(request,'login.html',context)

#  def second(request):
#     return render(request,'./second.html')

