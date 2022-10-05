from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.decorators import login_required

from .models import Host, Message
from account.models import User
from .forms import MessageForm

from tools.hashs import enced, deced

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
    

def room_view(request, pk):
    template = 'chat/room.html'
    if request.method == 'GET':

        context = {
            'form': MessageForm,
            'groups': Host.objects.filter(members_id=request.user.id),
            'room': get_object_or_404(Host, members_id=request.user.id, pk=pk)
        }

        return render(request, template, context)

