from rest_framework.decorators import api_view
from rest_framework.response import Response
from Create.models import Record
from .serializers import RecordSerializers

@api_view(['GET'])
def getroutes(request):
    routes = [
        'GET /api'
        'GET /api/record'
        'GET /api/record/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getrecords(request):
    records = Record.objects.all()
    serializer = RecordSerializers(records, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getrecord(request, pk):
    record = Record.objects.get(id=pk)
    serializer = RecordSerializers(record, many=False)
    return Response(serializer.data)