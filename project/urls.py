"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls',namespace="sign_up")),
    path('admin/', admin.site.urls),
    path('', include('job.urls',namespace="basic_job")),
    path('contact/', include('contact.urls',namespace="contact")),

]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# • To make form this is steps :
#    1- Make Model which have fileds in frontend
#    2- register this model in admin.py
#    3- make form for model as the auhor will reciept the msg in gmail
#    4- in this form will make :
#           ○-> import forms from django 
#           ○-> the model from models 
#           ○-> make class and inhirit forms.modelForm
#           ○-> make class Meta:
#           ○->         model=modelname you make form for it
#           ○->         fields = ['columns name']
#    5- go to views and import this form that you make : 
#           ○-> make in the page where the form in :
#           ○-> make if the client send post check validation and send to email
#           ○-> make else : dont make thing

#    
#    
#    
#    