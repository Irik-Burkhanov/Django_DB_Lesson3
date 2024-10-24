from audioop import reverse
from msilib.schema import ListView
from string import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from computer_hardware_store.models import Computer
from django_filters.views import FilterView
from computer_hardware_store import filters

# class ComputersListTemplateView(TemplateView):
#     template_name = 'computer_workshop/computers_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['computers'] = Computer.objects.all()
#         return context

class ComputersList(FilterView):
    template_name = 'computer_workshop/computers_list.html'
    model = Computer
    context_object_name = 'computers'
    filterset_class = filters.Computer

class ComputersDetail(DetailView):
    template_name = 'computer_workshop/computer_detail.html'
    model = Computer
    context_object_name = 'computer'

class ComputersUpdate(UpdateView):
    template_name = 'computer_workshop/computer_form.html'
    model = Computer
    fields = ['title', 'builder', 'description']

    def get_success_url(self):
        return reverse_lazy('computer_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        r = super(ComputersUpdate, self).form_valid(form)
        print(Computer.objects.all())
        return r

class ComputersCreate(CreateView):
    template_name = 'computer_workshop/computer_create.html'
    model = Computer
    fields = ['title', 'builder', 'description', 'image', 'id_pc']

    def get_success_url(self):
        return reverse_lazy('computer_detail', kwargs={'pk': self.object.pk})


class ComputersDelete(DeleteView):
    model = Computer
    template_name = 'computer_workshop/computer_delete.html'
    success_url = reverse_lazy('computers_list')