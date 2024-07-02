from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'website/index-8.html')

def about_view(request):
    return render(request,'website/about.html')    

def srvice_view(request):
    return render(request,'website/services.html')

def contact_view(request):
    return render(request,'website/contact.html')