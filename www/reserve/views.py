from django.views import generic
from rest_framework import viewsets, permissions

from .models import Reserve

# Create your views here.
from .serializers import ReserveSerializer


class IndexView(generic.ListView):
    template_name = 'reserve/index.html'
    context_object_name = 'field_list'

    def get_queryset(self):
        return Reserve.objects.order_by('created_at')


class ReserveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reserve.objects.order_by('created_at')
    serializer_class = ReserveSerializer
    permission_classes = [permissions.IsAuthenticated]
