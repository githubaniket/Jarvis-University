from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register', views.register),
    path('saveuser', views.saveuser),
    path('login', views.login),

    path('user/' , include('User.urls')),
    path('question/' , include('Question.urls'))
]
