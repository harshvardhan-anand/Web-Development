from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student

# Create your views here.
@api_view(['GET'])
def homepage(request):
    data = Student.objects.all()
    serializer = StudentSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dethomepage(request, pk):
    data = Student.objects.get(pk=pk)
    serializer  = StudentSerializer(data, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def post(request):
    # if data is form data then we use request.POST else we use request.data
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
    tobeupdated = Student.objects.get(pk=pk)
    serializer = StudentSerializer(data=request.data, instance=tobeupdated)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    tobedeleted = Student.objects.get(pk=pk)
    print(tobedeleted)
    tobedeleted.delete()
    return Response("Its deleted successfully")