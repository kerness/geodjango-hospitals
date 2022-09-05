from rest_framework import viewsets
from django.contrib.gis.db.models.functions import Area
from .models import Boundary
from .serializers import BoundarySerializer

class BoundaryViewSet(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer

    def get_queryset(self):
        return Boundary.objects.annotate(area=Area('mpoly')).order_by('area')
