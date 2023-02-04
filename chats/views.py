from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
import datetime
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Index(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = User


@login_required
def chatPage(request,username):
    now = datetime.datetime.now()
    users = User.objects.all()
    user = User.objects.get(username=username)
    chatUser = [request.user.username,username]
    chatUser.sort()
    chatUser = ''.join(chatUser)
    messages = Message.objects.filter(room=chatUser).order_by('timestamp')
    return render(request,'chatpage.html',{'username':username,'now':now,'messages':messages,'users':users,'user':user})

