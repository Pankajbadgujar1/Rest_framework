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
    serializer = StudentSerializer(data = request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status': 403, 'errors':serializer.errors, 'message':'Something went wrong'})
    
    serializer.save()
    return Response({'status': 200, 'payload': data, 'message':'your data  sent'})


@api_view(['PATCH'])
def update_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        data = request.data
        serializer = StudentSerializer(student_obj,data = request.data, partial = True)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'errors':serializer.errors, 'message':'Something went wrong'})
        
        serializer.save()
        return Response({'status': 200, 'payload': data, 'message':'your data  sent'})
    
    except Exception as e:
        return Response({'status':403, 'message':'invalid id'})
    
@api_view(['DELETE'])
def delete_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status': 200, 'message':'deleted'})
    
    except Exception as e:
        return Response({'status':403, 'message':'invalid id'})
     