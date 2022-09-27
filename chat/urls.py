from django.urls import path
from django.views.generic import TemplateView

from .views import (
    HostListView,
    HostDetailView
)

urlpatterns = [
    path('', HostListView.as_view()),
    path('msgs/<pk>', HostDetailView.as_view())
]

