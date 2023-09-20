from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
@api_view(['GET'])
def get_details(request):
    get_students=Student.objects.all()
    serialized_students=StudentSerializer(get_students,many=True)
    return Response({'status': 'success', "students":serialized_students.data}, status=200) 

@api_view(['POST'])
def add_student(request):
    if request.method=='POST':
        student_serializer=StudentSerializer(data=request.data)
        print(student_serializer)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'status':'success',"students":student_serializer.data},status=200)
        else:
            return Response({'status':'error','data':student_serializer.errors},status=404)
        
@api_view(['GET','DELETE','PUT'])
def edit_student(request,id):
    get_student=Student.objects.get(pk=id)

    if request.method=='PUT':
        serializer=StudentSerializer(get_student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success',"students":serializer.data},status=200)
        return Response({'status':'failed',"students":serializer.error},status=400)

    if request.method=='GET':
        serializer=StudentSerializer(get_student)
        return Response({'status': 'success', "students":serializer.data}, status=200)

    if request.method=='DELETE':
        get_student.delete()
        return Response(status=204)
