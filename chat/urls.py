from django.urls import path
from django.views.generic import TemplateView

from .views import (
    HostListView,
    HostDetailView
)

urlpatterns = [
    path('', HostListView.as_view()),
    path('msgs/', HostDetailView.as_view()),
    path('test', TemplateView.as_view(template_name='chat/room.html'))
]

