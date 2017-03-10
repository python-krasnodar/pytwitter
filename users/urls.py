from django.conf.urls import url
from .views import UserListView, UserDetailView

urlpatterns = [
    url(r'^$', UserListView.as_view(), name='users_list'),
    url(r'^(?P<slug>[\w\-]+)/$', UserDetailView.as_view(), name='users_detail'),
]
