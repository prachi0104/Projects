from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from resumebuilder.settings import *
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

# Create your views here.

    

def personalinfoview(request):
    context={}
    p_form=ResumeForm(request.POST or None)
    if p_form.is_valid():
        p_form.save()
        return redirect('download')
    else:
        context['form']=p_form
    return render(request,'pi.html',context)

def download(request):
    context={}
    context['data']=Resume.objects.all()
    return render(request,'download.html',context)


def sendemailview(request):
   context={}
   if request.method=="POST":
       form=SendemailForm(request.POST)
       if form.is_valid():
            name=form.cleaned_data['name']
            to_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, None, [to_email])
            context['data']=Resume.objects.filter(id=name.id)
            html_message=render_to_string('download.html',context)
            plain_msg=strip_tags(html_message)
            msg = EmailMultiAlternatives(subject, plain_msg, EMAIL_HOST_USER, [to_email])
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            return render(request, 'pi.html',context={'form':ResumeForm()})
   else:
           form = SendemailForm()
   return render(request, 'send.html', context={'form': form})



def updateresume(request, id):
    context = {}
    obj = get_object_or_404(Resume, id=id)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
           
            return redirect('download')
    else:
        form = ResumeForm(instance=obj)  

    context['form'] = form
    context['obj'] = obj
    context['id']=id
    return render(request, 'updateresume.html', context)













