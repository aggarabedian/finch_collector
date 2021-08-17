from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Record
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
  template_name = "home.html"

class About(TemplateView):
  template_name = "about.html"

class Records(TemplateView):
  template_name = "record_list.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    title = self.request.GET.get("title")

    if title != None:
      context["records"] = Record.objects.filter(title__icontains=title)
      context["header"] = f"Searching for {title}"
    else:
      context["records"] = Record.objects.all()
      context["header"] = "All Albums"
    return context

class RecordCreate(CreateView):
  model = Record
  fields = ["title", "img", "artist", "year"]
  template_name = "record_create.html"
  
  def get_success_url(self):
    return reverse("record_detail", kwargs={'pk': self.object.pk})

class RecordDetail(DetailView):
  model = Record
  template_name = "record_detail.html"


class RecordUpdate(UpdateView):
  model = Record
  fields = ["title", "img", "artist", "year"]
  template_name = "record_update.html"
  
  def get_success_url(self):
    return reverse("record_detail", kwargs={'pk': self.object.pk})

class RecordDelete(DeleteView):
  model = Record
  template_name = "record_delete_confirmation.html"
  success_url = "/records/"