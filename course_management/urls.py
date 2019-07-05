from django.urls import path

from .views import SubjectAdd, SubjectList, StudentList


app_name = 'course_management'

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject_list'),
    path('subjects/add/', SubjectAdd.as_view(), name='subject_add'),
    path('students/', StudentList.as_view(), name='student_list'),
]
