from django.urls import path
from website.views import *
app_name='website'
urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('service',srvice_view,name='service'),
    path('service_details',service_details_view,name='service_details'),
    path('contact',contact_view,name='contact'),
]