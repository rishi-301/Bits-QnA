from django.urls import path, include

from users.models import Profile
from .views import UserRegisterView, profile, profileupdate, InitialProfileUpdate
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/update', profileupdate, name='profile-update'),
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout',auth_views.LogoutView.as_view(), name='logout'),
    path('profile/initial',InitialProfileUpdate, name='initial_profile'),
    
   ]


