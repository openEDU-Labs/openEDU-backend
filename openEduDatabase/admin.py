from django.contrib import admin

from .models import Teacher, Student, Course, StudentInCourse, Lecture, Breakpoint, BreakpointScore


class CourseInline(admin.StackedInline):
	model = Course
	extra = 0

class TeacherAdmin(admin.ModelAdmin):
	inlines = [CourseInline]
	list_display = ('teacher_name', 'teacher_school')

class StudentInCourseInline(admin.StackedInline):
	model = StudentInCourse
	extra = 5

class CourseAdmin(admin.ModelAdmin):
	inlines = [StudentInCourseInline]
	list_display = ('course_name', 'teacher','course_description')

class StudentAdmin(admin.ModelAdmin):
	list_display = ('student_name', 'student_school')

class BreakpointInline(admin.StackedInline):
	model = Breakpoint
	extra = 2

class LectureAdmin(admin.ModelAdmin):
	list_display = ('lecture_name', 'course', 'get_teacher_name')
	search_fields = ['lecture_name']
	inlines = [BreakpointInline]

class StudentInCourseAdmin(admin.ModelAdmin):
	list_display = ('student', 'course')

class BreakpointScoreInline(admin.StackedInline):
	model = BreakpointScore
	extra = 2

class BreakpointAdmin(admin.ModelAdmin):
	list_display = ('breakpoint_name', 'get_course_name', 'get_teacher_name')
	inlines = [BreakpointScoreInline]


	


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(StudentInCourse, StudentInCourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(BreakpointScore)
admin.site.register(Breakpoint, BreakpointAdmin)