from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('logout/', views.logout_page, name='logout'),
]