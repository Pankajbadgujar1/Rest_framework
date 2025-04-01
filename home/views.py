from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.

@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)
    return Response({'status':200, 'message':'Hello django rest framework' , 'paylaod':serializer.data})


@api_view(['POST'])
def post_student(request):
    data = request.data
    print(data)
    return Response({'status': 200, 'payload': data, 'message':'you sent'})