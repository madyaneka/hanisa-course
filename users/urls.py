from django.urls import path

from users.views import UserList, UserAdd

app_name = 'users'

urlpatterns = [
    path('', UserList.as_view(), name='list'),
    path('add/', UserAdd.as_view(), name='add'),
]
