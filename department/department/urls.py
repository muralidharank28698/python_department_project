"""insertlogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",include("insertlogin.urls")),
    path('',views.index,name='index'),

    # path('',views.insertrecord,name='insertrecord'),
    # path('second/',views.second)
    path('department/',views.department,name='department'),
    path('about/',views.about,name='about'),
    path('ece/',views.ece,name='ece'),
    path('eee/',views.eee,name='eee'),
    path('cse/',views.cse,name='cse'),
    path('it/',views.it,name='it'),
    path('me/',views.me,name='me'),
    path('ce/',views.ce,name='ce'),
    path('mathematics/',views.mathematics,name='mathematics'),
    path('chemistry/',views.chemistry,name='chemistry'),
    path('csefaculty/',views.csefaculty,name='csefaculty'),
    path('csesyllabus/',views.csesyllabus,name='csesyllabus'),
    path('csefacility/',views.csefacility,name='csefacility'),

    # path('about/',views.about,name='about')


]
