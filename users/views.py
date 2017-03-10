from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'


class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'users/user_detail.html'
