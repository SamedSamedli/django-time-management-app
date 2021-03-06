from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout),
    path('add-todo/', views.add_todo),
    path('add-blocklist/', views.create_Blocklist),
    path('delete-todo/<int:id>', views.delete_todo),
    path('delete-blocklist/<int:id>', views.delete_blocklist),
    path('change-status/<int:id>/<str:status>', views.change_todo),
]
