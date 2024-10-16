from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.apiOverview, name="Api Overview"),
    path("list/", views.taskList, name="list"),
    path("detail/<int:id>/", views.taskDetail, name="Detail"),
    path("update/<int:id>/", views.taskUpdate, name="Update"),
    path("create/", views.taskCreate, name="Create"),
    path("delete/<int:id>", views.taskDelete, name="Delete"),
]
