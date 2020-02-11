from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from App1.models import Student


def hello(request):
    templates = loader.get_template('hello.html')
    context = {
        'name': 'ZhangSan',
    }
    result = templates.render(context=context)
    return HttpResponse(result)


def add_student(request):
    student = Student()
    student.s_name = 'LiSi'
    student.s_age = 19
    student.save()
    return HttpResponse('Add Success!')


def update_student(request):
    student = Student.objects.get(pk=1)
    student.s_name = 'LLLLLL'
    student.s_age = 29
    student.save()
    return HttpResponse('Student Update Success!')