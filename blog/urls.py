from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='homepage'),
    path('', views.home, name='homepage'),
    # path('', views.post_list, name='post_list'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('blog', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]