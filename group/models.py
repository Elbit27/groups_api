from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return f'Mr./Mrs. {self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, related_name='groups')

    def __str__(self):
        return self.title
