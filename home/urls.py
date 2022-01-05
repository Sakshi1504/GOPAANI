from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.search),
    #path('search', views.search)
]
