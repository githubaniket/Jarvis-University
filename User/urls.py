from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('logout', views.logout),
    path('ask', views.askque),
    path('viewque', views.viewque),
    path('profile', views.profile),
    path('changepass', views.changepass)
    
]
