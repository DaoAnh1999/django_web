from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('nhapcau/',views.nhapcau, name='nhapcau'),
    path('cauhoi/',views.cauhoi, name='cauhoi'),
]