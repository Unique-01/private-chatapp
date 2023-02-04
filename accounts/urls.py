from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup/',views.signUp,name="signup"),
    path('accounts/profile_update/',views.profileUpdate,name="profile_update")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)