from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('profile', views.viewprofile, name='viewprofile'),
    path('edit/<id>', views.editprofile, name='editprofile'),
    path('update', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete')
]


