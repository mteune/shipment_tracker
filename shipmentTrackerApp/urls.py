from django.urls import path, include
from . import views





urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login), 
    path('ships', views.ships),
    path('logout', views.logout),
    path('ships/create', views.create_ship),
    path('addship', views.addship),
    path('view/<int:ship_id>/', views.view),
    path('update/<int:ship_id>/', views.update),
    path('delete/<int:ship_id>/', views.delete),
    path('profile/<int:user_id>/', views.profile),
    path('updateprofile/<int:user_id>/', views.updateprofile),
    path('profilepic/<int:user_id>/', views.profilepic),
    path('updateprofilepic/<int:user_id>/', views.updateprofilepic),
    path('logout', views.logout)


]

