from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Host
from account.models import User

# Create your views here.


class HostListView(ListView):
    model = Host    
    template_name = "chat/groups.html"

    def get_queryset(self):
        return Host.objects.filter(members_id=self.request.user.id)
    
    # queryset = Host.objects.filter(members_id=request.user.id)


class HostDetailView(DetailView):
    model = Host
    template_name = "chat/room.html"
    

