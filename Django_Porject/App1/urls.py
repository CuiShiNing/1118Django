from django.conf.urls import url

from App1 import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^addstudent/', views.add_student),
    url(r'^updatestudent/', views.update_student),

]