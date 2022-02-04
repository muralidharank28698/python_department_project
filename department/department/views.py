from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from department.models import Faculty
# from department.models import Register
from django.contrib import messages
from .models import Faculty
# from .models import Register
# import RequestContext
# from django.contrib.auth    
from django.contrib.auth.models import User, auth
# from .forms import Formregister

# import base64


def index(request):
    return render(request,'index.html')



def department(request):
    # return HttpResponse("<h1>Hello Muralidharan...</h1>")
    # return render(request,'login.html')
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
    results = Faculty.objects.all()
    return render(request,'./csefaculty.html', {'Faculty':results})
    # return render(request,'./csefaculty.html')

def csesyllabus(request):
    return render(request,'./csesyllabus.html')

def csefacility(request):
    return render(request,'./csefacility.html')

    
def departmentPortal(request):
    return render(request,'./departmentPortal.html')

def staffstud(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()
        print('user created...')
        return redirect('login')
        # return render(request,'./login.html')

        # if request.POST.get('uname') and request.POST.get('position') and request.POST.get('email') and request.POST.get('password'):
        #     saverecord = Register()
        #     saverecord.uname = request.POST.get('uname')
        #     saverecord.position = request.POST.get('position')
        #     saverecord.email = request.POST.get('email')
        #     saverecord.password = request.POST.get('password')
        #     saverecord.save()
        #     messages.success(request,'record saved....')
        #     return render(request,'./staffstud.html')
    else:
        return render(request,'./staffstud.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            if (username == 'Student'):
                return redirect("studentportalpage")
            elif (username == 'Staff'):
                return redirect("staffportalpage")

            # return render(request,'./studentportalpage.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect("login")



    else:
        return render(request,'./login.html')


    #     try:
    #         Userdetails = Register.objects.get(mailid = request.POST['mailid'],password = request.POST['password'])
    #         print("username =",Userdetails)
    #         # print(userdetials)
            
    #         request.session['mailid'] = Userdetails.mailid
    #         # request.session['password'] = userdetials.password
    #         return render(request,'./studentportalpage.html')
    #     except Register.DoesNotExist as e:
    #         messages.success(request,'login failed')
    # return render(request,'./login.html')


    # return render(request,'./login.html')
    # if request.method == 'post':
    #     mailid = request.POST['mailid']
    #     password = request.POST['password']

        # saverecord = user.authenticate(mailid=mailid,password=password)

    # else:
# def insertrecord(request):
#     form = Formregister(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {'Formregister':Formregister}
#     return render(request,'login.html',context)

#  def second(request):
#     return render(request,'./second.html')

def studentportalpage(request):
    return render(request,'./studentportalpage.html')
def staffportalpage(request):
    return render(request,'./staffportalpage.html')