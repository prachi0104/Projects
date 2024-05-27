from django.shortcuts import render,redirect
from .forms import *
from .models import *



# Create your views here.


def home(request):
    labels=[]
    data=[]
    queryset=ItemModel.objects.order_by('-qty')[:5]
    for i in queryset:
        labels.append(i.product)
        data.append(i.qty)
    

    labels2=[]
    data2=[]
    queryset2=ItemModel.objects.order_by('qty')[:5]
    for y in queryset2:
        labels2.append(y.product)
        data2.append(y.qty)


    labels3=[]
    data3=[]
    queryset3=ItemModel.objects.all()
    for z in queryset3:
        labels3.append(z.product)
        data3.append(z.qty)

    return render(request, 'home.html',{
        'labels':labels,
        'data':data,
        'labels2':labels2,
        'data2':data2,
        'labels3':labels3,
        'data3':data3,


    })


    #return render(request,'home.html')


def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')


def kitcheninventory(request):
    #return render(request,'kinv.html')
    return render(request,'home.html')


def addinventory(request):
    context={}
    form=Userinventory(request.POST or None)
    if form.is_valid():
        form.save()
        data=ItemModel.objects.all()
        context['data']=data
        return render(request,'addinventory.html',{'form':Userinventory(),'data':data})
    else:
        form = Userinventory()

    data=ItemModel.objects.all()
    context['data']=data
    context['form']=form
    return render(request,'addinventory.html',{'form':form,'data':data})


def showinv(request):
    data=ItemModel.objects.all()
    return render(request, 'showinv.html', {'data':data})

def updateinv(request,id):
    context={}
    data=ItemModel.objects.get(id=id)
    formdata=Userinventory(request.POST or None,instance=data)
    if formdata.is_valid():
        formdata.save()
        return redirect('showinv')
    context['form']=formdata
    return render(request,'updateinv.html',context)


def deleteinv(request,id):
    printdata=ItemModel.objects.get(id=id)
    printdata.delete()
    data=ItemModel.objects.all()
    return render(request, 'showinv.html', {'data':data})


def monthlyinv(request):
    context={}
    form=MonthlyForm(request.POST or None)
    if form.is_valid():
        form.save()
        data=MonthlyList.objects.all()
        context['data']=data
        return render(request,'monlist.html',{'form':MonthlyForm(),'data':data})
    else:
        form=MonthlyForm()

    data=MonthlyList.objects.all()
    context['data']=data
    context['form']=MonthlyForm()
    return render(request,'monlist.html',{'form':form,'data':data})


def printlist(request):
    context={}
    data=MonthlyList.objects.all()
    context['data']=data
    return render(request,'printlist.html',{'data':data})



def logout(request):
    if 'name' in request.session:
        del request.session['name']
        return redirect('login')
    else:
        return redirect('login')
    


def contactdetails(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact_data=Contact(name=name,email=email,message=message)
        contact_data.save()
        return redirect('contactdetails')
    return render(request,'contact.html')


    
   




