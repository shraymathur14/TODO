from django.urls import path
from . import views

app_name = 'details'

urlpatterns=[
    path('',views.index, name="home"),
    path('display/', views.show, name="display"),
    path('delete/<str:task>', views.delete, name="delete")
]