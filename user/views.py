from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate # authenticate, aldığı username ve password bilgisine göre kullanıcının olup olmadığını sorgulayacak. kullanıcı yok ise none dönecek
# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None) # eğer post değil get request olursa bu form None olarak atanacak. Böylelikle get ya da post request olsa dahi form oluşacak.
    # eğer get request olursa None olacak böylelikle is_valid kontrolü yapılamıcak ve direkt kayıt ekranına yönlendirilecek.
    if form.is_valid(): # parolalar eşleşiyormu vs. diye form.is_valid() kullanıldı
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password") # eğer uyuşuyor ise username ve parolayı alıyor
        
        newUser = User(username=username) # newUser oluşturuldu 
        newUser.set_password(password)

        newUser.save() # newUser kayıt edildi.
        login(request,newUser) # daha sonra login işlemi yapıldı ve index sayfasına yönlendirildi.
        messages.info(request,"Başarıyla kayıt oldunuz..")

        return redirect("index")
    
    context = {
            "form": form
        }
    return render(request,"register.html",context) # tekrardan aynı sayfaya yönlendirildi
    

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı...")
            return render(request,"login.html",context)
            
        messages.success(request,"Başarıyla giriş yaptınız..")
        login(request,user)
        return redirect("index")
     
    return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    return redirect("index")