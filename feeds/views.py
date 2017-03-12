from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from .models import Feed


@method_decorator(login_required, name='dispatch')
class IndexDetailView(ListView):
    model = Feed
    template_name = 'feeds/index.html'

    def get_queryset(self):
        return Feed.objects.filter(user_id=self.request.user.id)
