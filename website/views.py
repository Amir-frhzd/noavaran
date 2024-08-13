from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.
def index_view(request):
    return render(request,'website/index-8.html')

def about_view(request):
    return render(request,'website/about.html')    

def srvice_view(request):
    return render(request,'website/services.html')

def service_details_view(request):
    return render(request,'website/services-details.html')

def contact_view(request):
    if request.method =='POST':
        form=ContactForm(request.POST)
        print("55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555")
        if form.is_valid():
            phone=form.cleaned_data['phone']
            if not phone.startswith('09'):
                messages.add_message(request,messages.ERROR,"شماره موبایل باید با 09 شروع شود لطفا فرم را دوباره وارد کنید با تشکر")
                return redirect('website:contact')
            if len(phone) !=11:
                messages.add_message(request,messages.ERROR,"شماره موبایل باید دقیقا 11 رقم باشد لطفا فرم را دوباره وارد کنید با تشکر")
                return redirect('website:contact')

            form.save()
            messages.add_message(request,messages.SUCCESS,'فرم با موفقیت ثبت شد با تشکر از شما',fail_silently=True)
            print("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999")
        else:
             messages.add_message(request,messages.ERROR,"اطلاعات را به صورت کامل و به درستی وارد کنید")
    form=ContactForm()
    context={'form':form}
    return render(request,'website/contact.html',context)
def custom_404(request,exception):
    return redirect('/')