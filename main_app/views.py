from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Record

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