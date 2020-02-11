from django.db import models

class Grade(models.Model):
    g_name = models.CharField(max_length=32)

class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class PersonManager(models.Manager):
    def get_queryset(self):
        return super(PersonManager, self).get_queryset().filter(p_delete=True)

    def create(self, p_name, p_age=99, p_sex=True):
        person = self.model()
        person.p_name = p_name
        person.p_age = p_age
        person.p_sex = p_sex
        return person


class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True, db_column='name')
    p_age = models.IntegerField(default=18, db_column='age')
    # sex 默认为男，True为女
    p_sex = models.BooleanField(default=True, db_column='sex')
    p_delete = models.BooleanField(default=True)
    objects = PersonManager()

    # 表重命名
    class Meta:
        db_table = 'People'

    @classmethod
    def create(cls, p_name, p_age=99, p_sex=True):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex)

class Order(models.Model):
    o_name = models.CharField(max_length=16)
    o_time = models.DateTimeField(auto_now_add=True)