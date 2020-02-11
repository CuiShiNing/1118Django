import random

from django.db.models import Max, Avg
from django.http import HttpResponse
from django.shortcuts import render

from App2.models import Student, Grade, Person, Order


def get_grade(request):
    student = Student.objects.get(pk=1)
    grade = student.s_grade
    return HttpResponse('grade %s' % grade.g_name)


def get_students(request):
    # grade = Grade.objects.get(pk=1)
    # students = grade.student_set.all()
    # students = Student.objects.filter(s_grade__g_name='python1801')
    students = Student.objects.all()
    grades = Grade.objects.filter(student__s_name='王六')
    context = {
        'grades': grades,
        'students': students,
    }
    return render(request, 'app2_student_list.html', context=context)


def inster_people(request):
    for i in range(15):
        person = Person()
        person.p_name = 'Tom%d' % i
        person.p_age = random.randrange(66)
        person.p_sex = i % 2
        person.save()
    return HttpResponse('创建成功！')


def get_persons(request):
    # persons = Person.objects.filter(p_age__gt=18).filter(p_age__lt=55)
    persons = Person.objects.exclude(p_age__lt=25).exclude(p_age__gt=50)
    # 进行排序
    persons = Person.objects.all().order_by('p_age')
    # 将数据转换成一个字典，再转换成列表， 后期可以装换成 Json（进行数据转换）
    persons_values = persons.values()
    context = {
        'persons': persons,
    }
    return render(request, 'app2_get_persons.html', context=context)
    # return render_to_response()


def add_person(request):
    # person = Person.create('ZhangSan')
    # person.save()
    person = Person.objects.create('LiSi')
    person.save()
    return HttpResponse('添加成功！')


def get_person(request):
    username = 'Tom9'
    userage = 28

    users = Person.objects.filter(p_name=username)
    if users.count():
        user = users.first()
        if user.p_age == userage:
            s = '匹配成功！'
        else:
            s = '年龄错误！'
    else:
        s = '用户名不存在！'
    return HttpResponse(s)


def get_orders(request):
    # 关闭Django项目中的时区(settins中UEE_TZ = False)，使用数据库中的时区
    orders = Order.objects.filter(o_time__month=2)
    for order in orders:
        print(order.o_name)
    return HttpResponse('获取成功！')


def get_max_age(request):
    person = Person.objects.aggregate(Max('p_age'))
    person = Person.objects.aggregate(Avg('p_age'))
    print(person)
    return HttpResponse('获取成功！')


def zy2index(request):
    return render(request, 'zy2index.html')