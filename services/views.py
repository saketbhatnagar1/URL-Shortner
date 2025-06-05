from django.shortcuts import render, redirect
import random,string
from .models import Url
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site


def getAlias():
    return "".join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8)])


# Create your views here.
def dashboard(request):
    if request.method == "POST":
        
        URL = request.POST["URL"]
        alias = request.POST.get("Alias",None)
        print(alias,"Fetch")
        if not alias:
            alias = getAlias()
            print(alias,"Generated")
        try:
            #request.user.url_set(target_url=url)
            Url.objects.create(user=request.user, target_url=URL, alias=alias)
            print("object getting created")
            messages.success(request,"Url shortened successfully")
            return redirect("dashboard")
        except:
            messages.error(request,"Alias In Use please select different alias")
            print("error")
            return render(request,"dashboard.html",{"url":URL,"alias":alias})

    site = get_current_site(request)
    return render(request,'dashboard.html',{"domain":site})
    

def redirect_to_target_page(request,alias):
    obj = Url.objects.get(alias=alias)
    URL = obj.target_url
    return redirect(URL)