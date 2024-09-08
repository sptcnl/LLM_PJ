from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("create/", views.create, name="create"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
]