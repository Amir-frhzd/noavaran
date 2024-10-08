from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import *
app_name='accounts'
urlpatterns = [
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('logout',logout_view,name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',success_url = reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),
        
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]