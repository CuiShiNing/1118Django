
from django.conf.urls import url
from django.urls import path

from App2 import views

urlpatterns = [
    url(r'^getgrade/', views.get_grade),
    url(r'^getstudents/', views.get_students),
    url(r'^insterperson/', views.inster_people),
    url(r'^getpersons/', views.get_persons),
    url(r'^addperson/', views.add_person),
    url(r'^getperson/', views.get_person),
    url(r'^getorders/', views.get_orders),
    url(r'^getmaxage/', views.get_max_age),
    url(r'^zy2base/', views.zy2base),
    url(r'^zy2index/', views.zy2index),
    url(r'^zy2about/', views.zy2about),
    # path(r'zy2about/', views.zy2about, name='zy22about'),
    url(r'^zy2listpic/', views.zy2listpic),
    url(r'^zy2newlistpic/', views.zy2newlistpic),
    url(r'^head/', views.head),


]

