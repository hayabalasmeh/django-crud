from django.shortcuts import render
from .models import Snack
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from django.urls import reverse_lazy

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title','purchaser', 'description']

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['title','purchaser', 'description']

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')