from django.urls import path
from user import views

urlpatterns = [
    path('h/', views.h),
    path('j/', views.j),
    path('l/', views.l),
    path('d/', views.d),
    path('c/', views.c),
]
