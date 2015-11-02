from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from .models import Teacher, Course, Lecture, Student, StudentInCourse, Breakpoint, BreakpointScore
from django.db.models.query import QuerySet

from django.core import serializers

## future note: I can get specific fields using: 
#data = serializers.serialize('xml', SomeModel.objects.all(), fields=('name','size'))

## gets information about a specific teacher
def get_teacher(request, teacher_id):
	teacher = get_object_or_404(Teacher, pk=teacher_id)
	return response(Teacher.objects.all().filter(id = teacher.id))

## gets a list of courses from the teacher
def get_teacher_courses(request, teacher_id):
	teacher = get_object_or_404(Teacher, pk=teacher_id)
	return response(Course.objects.all().filter(teacher_id = teacher.id))

## gets a list of lectures from the course
def get_course_lectures(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	return response(Lecture.objects.all().filter(course_id = course.id))

## gets students in a particular course
def get_course_students(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	return response(StudentInCourse.objects.all().filter(course_id = course.id))

## gets breakpoints for a particular lecture
def get_lecture_breakpoints(request, lecture_id):
	lecture = get_object_or_404(Lecture, pk=lecture_id)
	return response(Breakpoint.objects.all().filter(lecture_id = lecture.id))

## gets breakpoint scores for a particular breakpoint
def get_breakpoint_scores(request, breakpoint_id):
	breakpoint = get_object_or_404(Breakpoint, pk=lecture_id)
	return response(BreakpointScore.objects.all().filter(breakpoint_id = breakpoint.id))

## gets student information
def get_student(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	return response(Student.objects.all().filter(id = student.id))

## gets courses for a particular student (technically student in course information) for a particular student
def get_student_courses(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	return response(StudentInCourse.objects.all().filter(student_id = student.id))

## gets breakpoint scores for a student in a course
def get_student_breakpoint_scores(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	student_in_course = get_object_or_404(StudentInCourse, pk=student.id)
	return response(BreakpointScore.objects.all().filter(student_in_course_id = student_in_course.id))

### HELPER METHODS
#helper method to clean things up
def response(query):
	return JsonResponse(serializers.serialize("json", query), safe=False)



