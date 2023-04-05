from rest_framework import viewsets
from rest_framework.response import Response
from .models import Resource
from .serializers import ResourceSerializer

class ResourceAPIView(viewsets.ViewSet):
    def list_gdd(self, request):
        gdd_resources = Resource.objects.filter(committee='GDD')
        serializer = ResourceSerializer(gdd_resources, many=True)
        return Response(serializer.data)
    
    def list_gad(self, request):
        gad_resources = Resource.objects.filter(committee='GAD')
        serializer = ResourceSerializer(gad_resources, many=True)
        return Response(serializer.data)
    
    def list_gsd(self, request):
        gsd_resources = Resource.objects.filter(committee='GSD')
        serializer = ResourceSerializer(gsd_resources, many=True)
        return Response(serializer.data)
    
    def add_resource(self, request):
        if request.method == 'POST':
            serializer = ResourceSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return Response({'msg': 'Resource Added Successfully'})
            else:
                return Response({'msg': 'Failed To Add Resource'})