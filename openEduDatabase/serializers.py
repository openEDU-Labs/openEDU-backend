from rest_framework import serializers
from .models import Teacher, Course, Lecture, Breakpoint, BreakpointScore, Student

class TeacherSerializer(serializers.ModelSerializer):
	courses = serializers.PrimaryKeyRelatedField(many=True,  queryset=Course.objects.all())
	class Meta:
		model = Teacher
		fields = ('teacher_name', 'teacher_school', 'courses')

class CourseSerializer(serializers.ModelSerializer):
	teacher = TeacherSerializer()
	lectures = serializers.PrimaryKeyRelatedField(many=True, queryset=Lecture.objects.all())
	students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
	class Meta:
		model = Course
		fields = ('course_name', 'course_description', 'teacher', 'lectures', 'students') 

class LectureSerializer(serializers.ModelSerializer):
	course = CourseSerializer()
	breakpoints = serializers.PrimaryKeyRelatedField(many=True, queryset=Breakpoint.objects.all())
	class Meta:
		model = Lecture
		fields = ('lecture_name', 'lecture_description','breakpoints', 'course')
class BreakpointSerializer(serializers.ModelSerializer):
	breakpoint_scores = serializers.PrimaryKeyRelatedField(many=True, queryset=BreakpointScore.objects.all())
	lecture = LectureSerializer()
	class Meta:
		model = Breakpoint
		fields = ('breakpoint_name', 'breakpoint_description', 'lecture','breakpoint_scores')

class StudentSerializer(serializers.ModelSerializer):
	courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
	breakpoint_scores = serializers.PrimaryKeyRelatedField(many=True, queryset=BreakpointScore.objects.all())
	class Meta:
		model = Student
		fields = ('student_name', 'student_school', 'courses', 'breakpoint_scores')

class BreakpointScoreSerializer(serializers.ModelSerializer):
	student = StudentSerializer()
	breakpoint = BreakpointSerializer()
	class Meta:
		model = BreakpointScore
		fields = ('score','breakpoint', 'student', )