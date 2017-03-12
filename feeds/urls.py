from django.conf.urls import url
from .views import IndexDetailView

urlpatterns = [
    url(r'^$', IndexDetailView.as_view(), name='index'),
]
