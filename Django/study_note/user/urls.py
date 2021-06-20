from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('add/', views.add_note),
    path('show/', views.show_note),
    path('test/', views.test),
    path('page/', views.page),
    path('download/', views.download),
    path('upload/', views.upload),
    path('delete/', views.delete),
    path('update/', views.update),
]
