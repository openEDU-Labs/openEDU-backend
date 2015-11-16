from django.db import models

# Create your models here.
class Teacher(models.Model):
	teacher_name = models.CharField(max_length=50)
	teacher_school = models.CharField(max_length=50)
	def __str__(self):
		return self.teacher_name
class Student(models.Model):
	student_name = models.CharField(max_length=50)
	student_school = models.CharField(max_length=50)
	def __str__(self):
		return self.student_name

class Course(models.Model):
	course_name = models.CharField(max_length=50)
	course_description = models.CharField(max_length=1500)
	teacher = models.ForeignKey(Teacher, related_name='courses')
	students = models.ManyToManyField(Student, related_name='courses')
	def __str__(self):
		return self.course_name

class Lecture(models.Model):
	lecture_name = models.CharField(max_length = 50)
	lecture_description = models.CharField(max_length = 500)
	course = models.ForeignKey(Course, related_name='lectures')
	lecture_link = models.CharField(max_length=100)
	lecture_data = models.TextField()
	
	def __str__(self):
		return self.lecture_name
	def get_teacher_name(self):
		return self.course.teacher.teacher_name
	get_teacher_name.short_description = 'Teacher'
	

class Breakpoint(models.Model):
	breakpoint_name = models.CharField(max_length = 50)
	breakpoint_description = models.CharField(max_length = 500)
	lecture = models.ForeignKey(Lecture, related_name='breakpoints')
	
	def __str__(self):
		return self.breakpoint_name
	def get_course_name(self):
		return self.lecture.course.course_name
	def get_teacher_name(self):
		return self.lecture.course.teacher.teacher_name
	get_course_name.short_description = 'Course'
	get_teacher_name.short_description = 'Teacher'

class BreakpointScore(models.Model):
	student= models.ForeignKey(Student, related_name='breakpoint_scores')
	breakpoint = models.ForeignKey(Breakpoint, related_name='breakpoint_scores')
	score = models.IntegerField(default = 0)

	def __str__(self):
		return self.breakpoint.breakpoint_name + ' : ' + self.student.student_name

