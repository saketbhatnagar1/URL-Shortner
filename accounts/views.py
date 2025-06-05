from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        if username and password:
            user = auth.authenticate(request=request,username=username,password=password)
            if user:
                auth.login(request,user)
                messages.success(request,"lOGGED IN")
                return redirect("/")
            messages.error(request,"Incorrect credentials")
            return render(request,"login.html",{"username":username})
    return render(request,"login.html")
def register(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        email = request.POST.get("email",None)
        
        try:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            auth.login(request=request,user=user)
        except:
            messages.error(request,"Username exists please select Unique")
            return render(request,"register.html",{"username":username,"email":email})
        return redirect("/")
    return render(request,"register.html",{})
def logout(request):
    auth.logout(request)
    return redirect("login_view")