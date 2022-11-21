from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('ccu410420026', views.ccu410420026_function)
]
