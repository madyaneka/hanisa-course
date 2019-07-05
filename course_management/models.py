from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20, verbose_name='Subject')
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)
    grade = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='school')

    def __str__(self):
        return self.name