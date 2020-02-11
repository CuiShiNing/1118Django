
from django.conf.urls import url
from django.urls import path

from App2 import views

urlpatterns = [
    url('^getgrade/', views.get_grade),
    url('^getstudents/', views.get_students),
    url('^insterperson/', views.inster_people),
    url('^getpersons/', views.get_persons),
    url('^addperson/', views.add_person),
    url('^getperson/', views.get_person),
    url('^getorders/', views.get_orders),
    url('^getmaxage/', views.get_max_age),
    path('zy2index/', views.zy2index),
]

