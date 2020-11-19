from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('article2', views.s),
    path('article1', views.x),
    path('article3', views.y),
    path('article4', views.z),
    path('article5', views.zz),
    path('article6', views.ab),
    path('article7', views.bc),
    path('article8', views.cd),
    path('article9', views.de),
    path('article10', views.ef),
    path('article11', views.fg),
    path('article12', views.gh),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.loginPage, name='logout')
]