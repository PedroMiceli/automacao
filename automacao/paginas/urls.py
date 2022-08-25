from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('', views.login_usuario, name='login'),
    path('home/', views.home, name='home'),

]