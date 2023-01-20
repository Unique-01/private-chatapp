from django.urls import path,include
from . import views


urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup/',views.signUp,name="signup"),
    path('accounts/profile_update/',views.profileUpdate,name="profile_update")
]
