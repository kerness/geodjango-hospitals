from rest_framework import viewsets
from django.db.models import Sum
from .models import Hospital
from .serializers import HospitalSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    @action(detail=False, methods=['get'])
    def total_bed_capacity(self, request):
        bed_capacity = Hospital.objects.aggregate(bed_capacity=Sum('beds'))
        return Response(bed_capacity)