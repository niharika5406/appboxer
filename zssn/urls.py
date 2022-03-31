from django.urls import path
from . import views

urlpatterns = [
    path('survivors/', views.ZombieSurvivalSocialNetworkAPI.as_view()),
    path('survivors/<int:id>', views.ZombieSurvivalSocialNetworkAPI.as_view()),
    path('survivors/reports', views.show_percentage_reports),
]