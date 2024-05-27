from django.db import models

# Create your models here.


class Resume(models.Model):
    #Personal Details
    name=models.CharField(max_length=50,null=True)
    phn_no=models.IntegerField(null=True)
    email=models.CharField(max_length=50,null=True)
    address=models.TextField(null=True)
    nationality=models.CharField(max_length=50,null=True)
    dob=models.DateField(auto_now=False, auto_now_add=False,null=True)
    website=models.EmailField(max_length=254,null=True,blank=True)
    maritial_status=models.CharField(max_length=50,null=True)
    #objective
    details=models.TextField(null=True)
    #work experience
    company_name=models.CharField(max_length=50,null=True)
    job_title=models.CharField(max_length=50,null=True)
    start_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    end_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    desc=models.TextField(null=True)
    #projects
    project_name=models.CharField(max_length=50,null=True)
    project_title=models.CharField(max_length=50,null=True)
    p_start_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    p_end_date=models.DateField(auto_now=False, auto_now_add=False,null=True)
    p_desc=models.TextField(null=True)
    #education
    degree=models.CharField(max_length=50,null=True)
    s_degree=models.CharField(max_length=50,null=True,blank=True)
    school=models.CharField(max_length=50,null=True)
    grade=models.CharField(max_length=50,null=True)
    year_of_passing=models.IntegerField(null=True)
    #skills
    skill_name=models.TextField(null=True)


    def __str__(self):
        return self.name or "Unnamed Resume"
    


class SendEmail(models.Model):
    name=models.ForeignKey(Resume,on_delete=models.CASCADE)
    email=models.EmailField(max_length=254,)
    subject=models.CharField(max_length=50,default=None)
    message=models.TextField(default=None)
    



