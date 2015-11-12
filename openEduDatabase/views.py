from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from .models import Teacher, Course, Lecture, Student, Breakpoint, BreakpointScore

from rest_framework import generics
from rest_framework import viewsets
from .serializers import TeacherSerializer, CourseSerializer, LectureSerializer, BreakpointSerializer, StudentSerializer, BreakpointScoreSerializer

from django.core import serializers

from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route


class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	
class LectureViewSet(viewsets.ModelViewSet):
	queryset = Lecture.objects.all()
	serializer_class = LectureSerializer
class BreakpointViewSet(viewsets.ModelViewSet):
	queryset = Breakpoint.objects.all()
	serializer_class = BreakpointSerializer

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class BreakpointScoreViewSet(viewsets.ModelViewSet):
	queryset = BreakpointScore.objects.all()
	serializer_class = BreakpointScoreSerializer

