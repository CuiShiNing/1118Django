from django.conf.urls import url

from Article import views

urlpatterns ={
    url(r'^index/', views.index),
}