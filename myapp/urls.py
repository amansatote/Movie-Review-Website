from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name="index"),
    path("navbar", views.navbar, name='navbar'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('details', views.details, name='details'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    # path('checkout', views.checkout, name='checkout'),
    path('account', views.account, name='account'),
    # path('openDetail', views.openDetail, name='openDetail'),
]