from django.conf.urls import url
from django.urls import path, include
from aut import views

urlpatterns = [
    path('status/', views.status),
    path('', views.index),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', views.auth),
    path('accounts/profile/', views.profile),
    path('logout/', views.logout_view),
]

