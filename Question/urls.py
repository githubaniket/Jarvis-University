from django.urls import path
from . import views

urlpatterns = [
    path('save',views.saveQus),
    path('saveans',views.saveAns),
    path('viewans',views.viewAns)
]