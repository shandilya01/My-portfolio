
# creating the urls.py file inside our apps is useful if working with large apps

from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblog, name='allblog'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
