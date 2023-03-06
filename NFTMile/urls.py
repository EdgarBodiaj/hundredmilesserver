from django.urls import path
from . import views

urlpatterns = [
    path('editor/', views.editor, name='editor'),
    path('graph/', views.graph, name='graph'),
    path('Home/', views.index, name='index'),
]