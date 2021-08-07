from django.urls import path
from .views import home_view, login_view, logout_view, main_view, register_view, update_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('letschat', main_view, name='main_view'),
    path('register', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout', logout_view, name='logout_view'),
    path('home', home_view, name='home_view'),
    path('updateProfile', update_view, name='update_view'),
]
