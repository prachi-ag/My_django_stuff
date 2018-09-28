from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = models.School
    template_name = 'school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_detail.html'



