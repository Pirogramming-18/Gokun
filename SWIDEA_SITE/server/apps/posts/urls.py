# posts/urls.py

from django.urls import path
from . import views

urlpatterns= [
    path("", views.id_list, name='list'),
    path("posts/create", views.id_create, name='create'),
    path("posts/<int:pk>/update", views.id_update, name='update'),
    #path("posts/<int:pk>/delete", views.id_delete, name='delete'),
    path("posts/<int:pk>", views.id_detail, name='detail'),
]