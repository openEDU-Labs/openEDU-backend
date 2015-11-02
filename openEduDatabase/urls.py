from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_teacher/(?P<teacher_id>[0-9]+)/$', views.get_teacher),
    url(r'^get_teacher_courses/(?P<teacher_id>[0-9]+)/$', views.get_teacher_courses),
    url(r'^get_course_lectures/(?P<course_id>[0-9]+)/$', views.get_course_lectures),
    url(r'^get_student/(?P<student_id>[0-9]+)/$', views.get_student),
    url(r'^get_student_courses/(?P<student_id>[0-9]+)/$', views.get_student_courses),

]