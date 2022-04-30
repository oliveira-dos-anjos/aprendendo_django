from telnetlib import DET
from typing import List
from django.views.generic import DetailView, ListView

from . models import post


class PostListView(ListView):
    model = post


class PostDetailView(DetailView):
    model = post