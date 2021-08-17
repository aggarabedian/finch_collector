from django.urls import path
from . import views

urlpatterns = [
  path("", views.Home.as_view(), name="home"),
  path("about/", views.About.as_view(), name="about"),
  path("records/", views.Records.as_view(), name="record_list"),
  path("records/new/", views.RecordCreate.as_view(), name = "record_create"),
  path("records/<int:pk>/", views.RecordDetail.as_view(), name = "record_detail"),
  path("records/<int:pk>/update/", views.RecordUpdate.as_view(), name = "record_update"),
]