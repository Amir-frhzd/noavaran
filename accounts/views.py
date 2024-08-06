from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import Login_form,UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST" :
            form=Login_form(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username_or_email']
                password=form.cleaned_data['password']
                
                #password=form.cleaned_data['password']
                
                if '@' in username:
                    
                    username = User.objects.get(email=username).username
                else :
                    
                    username = username
                    
                user =authenticate(username=username,password=password)
                if user is not None:
                    
                    login(request,user)
                    next_url=request.GET.get('next')
                    print('NEXT URL : ',next_url)
                    messages.add_message(request,messages.SUCCESS,"با موفقیت وارد شدید")
                    if next_url :

                        return redirect(next_url)
                    else :
                        return redirect('/')
            
                else:
                    messages.add_message(request,messages.ERROR,"اطلاعات وارد شده اشتباه است")
                    #return redirect('/')            
        form=AuthenticationForm()
        context ={'form':form}
        
        return render(request,'accounts/login.html',context)
    else :
        
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
    

def signup_view(request):
    if request.method == 'POST' :
        username=request.POST['username']
        email=request.POST['email']
        if User.objects.filter(username=username).exists() :
            messages.error(request,'کاربری با این یوزرنیم قبلا ثبت نام کرده')
        if User.objects.filter(email=email).exists() :
            messages.error(request,'کاربری با این ایمیل قبلا ثبت نام کرده')
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"ثبت نام شما با موفقیت انجام شد")
            return redirect('accounts:login')
        else:
            messages.add_message(request,messages.ERROR,"مشکلی در ثبت نام بوجود آمده لطقا دوباره تلاش کنید")
            
    form=UserCreationForm()
    context={'form':form}
    return render(request,'accounts/signup.html',context)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('accounts:password_reset_done')