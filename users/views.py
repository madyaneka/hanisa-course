from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Create your views here.
class UserList(LoginRequiredMixin, ListView):
    model = CustomUser
    queryset = CustomUser.objects.filter(is_superuser=False)
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    login_url = 'home'


@method_decorator(staff_member_required, name='dispatch')
class UserAdd(CreateView):
    model = CustomUser
    template_name = 'users/user_form.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('users:list')


class UserUpdate(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/user_form.html'

    def get_success_url(self):
        return reverse('users:list')


class UserDelete(DeleteView):
    model = CustomUser
    template_name = 'users/user_delete.html'

    def get_success_url(self):
        return reverse('users:list')
