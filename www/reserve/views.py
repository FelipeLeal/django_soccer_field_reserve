from django.views import generic
from .models import Field, Reserve


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'reserve/index.html'
    context_object_name = 'field_list'

    def get_queryset(self):
        return Reserve.objects.order_by('created_at')
