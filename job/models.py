from django.db import models 
from django.utils.text import slugify

def image_dir(obj,filename):
    img_name=filename.split(".")
    img_name[0]=obj.id
    return f"jobs/{img_name[0]}.{img_name[1]}"

def cv_dir(obj,filename):
    cv_name=filename.split(".")
    cv_name[0]=obj.id
    return f"jobs/cvs/{cv_name[0]}.{cv_name[1]}"
    
class Category(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self) -> str:
        return self.name
# Create your models here.
job_type_choices=[
    ("Full_Time","Full_Time"),
    ("Part_Time","Part_Time")
                  ]

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    jop_type=models.CharField(max_length=100,choices=job_type_choices)
    description = models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=1)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experiece=models.IntegerField(default=1)
    category=models.ForeignKey("Category",on_delete=models.PROTECT)
    image=models.ImageField(upload_to=image_dir,null=0)
    slug=models.SlugField(blank=1,null=1)

    def save(self,*args, **kwargs) -> None:

        before = (self.title).lower().split(" ")
        self.slug = "-".join(before)
        self.slug = slugify(self.title)

        models.Model.save(self,*args,**kwargs)
    def __str__(self) -> str:
        return self.title
 
    
class job_applies(models.Model):
    job=models.ForeignKey(Job,related_name="apply_job",on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    web_link=models.URLField()
    cv=models.FileField(upload_to=cv_dir,null=0)
    covletter=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now=1)

    def __str__(self) -> str:
        return self.name
    

    