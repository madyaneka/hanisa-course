from django.contrib import admin

from .models import School, Student, Subject


# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Subject)
