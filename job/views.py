from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,AddJopForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def job_list(request):
    joblist=Job.objects.all()
    paginator = Paginator(joblist, 5)  # Show 2 contacts per page.
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={"jobs":page_obj}
    return render(request,"job/jobs.html",context)
@login_required
def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    if request.method=="POST":
        form=ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
            form=ApplyForm()
    else:
        form=ApplyForm()

    
    context={"job":job,'form':form}
    return render(request,"job/job_details.html",context)

@login_required
def add_job(request):
    if request.method=="POST":
        form = AddJopForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            form=AddJopForm()
            job_list(request)
    
    else:
        form=AddJopForm()

    
    context={'form':form}
    return render(request,"job/add_job.html",context)
