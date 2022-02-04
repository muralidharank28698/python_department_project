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
from django.conf import settings
from django.conf.urls.static import static
import base64

# from django.conf.urls import url, include

# from department.department import settings
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
    path('departmentPortal/',views.departmentPortal,name='departmentPortal'),
    path('login/',views.login,name='login'),
    path('staffstud/',views.staffstud,name='staffstud'),
    path('studentportalpage/',views.studentportalpage,name='studentportalpage'),
    path('staffportalpage/',views.staffportalpage,name='staffportalpage')

    # path('about/',views.about,name='about')
]

# urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns += urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# or

# urlpatterns = patterns('',
#     # ... the rest of your URLconf goes here ...
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# or

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))

        # or

# urlpatterns = [
#   url(r'^admin/', include(admin.site.urls)),
#   url(r'^', include(router.urls)),
#   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]