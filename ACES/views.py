from django.http import HttpResponse
from django.shortcuts import render,redirect
from service.models import service
from news.models import news
from django.core.paginator import Paginator
from member.forms import memberform
# from django.core.mail import send_mail



# from newregister.models import register



def home(request):
    # send_mail(
    #     'Testing Mail',
    #     'here is the message',
    #     'nepaldnes@gmail.com',
    #     ['deenez.npl1@gmail.com'],
    #     fail_silently=False

    # )

    st=""
    data={}
    servicedata = service.objects.all().order_by('-id')
    if request.method=="POST":
        st=request.POST['servicename']
        if st!=None:
            servicedata = service.objects.filter(service_title__icontains=st)
    
    newsdata=news.objects.all().order_by('id')  

    paginator=Paginator(servicedata,3)
    page_number=request.GET.get('page')
    servicedatafinal=paginator.get_page(page_number)
    totalpage=servicedatafinal.paginator.num_pages

    
    data={
        'servicedata1':servicedatafinal,
        'newsdata':newsdata,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)]
    }
    return render(request,"index.html",data)

# def newsdetail(request,newsid):
def newsdetail(request,news_slug):

    # newsdetails=news.objects.get(id=newsid)
    newsdetails=news.objects.get(news_slug=news_slug)

    data ={
        'newsdetails':newsdetails
    }

    return render(request,"newsdetail.html",data)


def register(request):
    if request.method=="POST":
        form=memberform(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,"contactus.html")

    else:
        return render(request,"contactus.html")




def formsubmit(request):
    return render(request,"formsubmit.html")


