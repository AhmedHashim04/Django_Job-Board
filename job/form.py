from django import forms

from .models import job_applies , Job 

class ApplyForm(forms.ModelForm):
    class Meta:
        model = job_applies
        fields = ['name', 'email','web_link','cv','covletter']

class AddJopForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','jop_type','description','vacancy','salary','experiece','image','category']
        

