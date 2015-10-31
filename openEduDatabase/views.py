from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from .models import Teacher, Course, Lecture

from django.core import serializers




#gets a list of courses from the teacher
def courses(request, teacher_id):
	teacher = get_object_or_404(Teacher, pk=teacher_id)
	return JsonResponse(serializers.serialize("json", 
		Course.objects.all().filter(teacher_id = teacher.id)), safe=False)

#gets a list of lectures from the course
def lectures(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	return JsonResponse(serializers.serialize("json", 
		Lecture.objects.all().filter(course_id = course.id)), safe=False)
