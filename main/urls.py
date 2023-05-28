from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.HomeView.as_view()),
    path('portfolio-item/<int:id_item>/', views.PortfolioItemView.as_view()),

]
