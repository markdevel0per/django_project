from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import SignInForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('sign-up/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign-in/', auth_views.LoginView.as_view(template_name='core/signin.html', authentication_form=SignInForm),
         name='signin'),
]
