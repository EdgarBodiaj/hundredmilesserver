from django.urls import path
from Database import views

urlpatterns = [
    path('data/', views.data_List),
    path('data/<int:group>/', views.data_List_Group)
]