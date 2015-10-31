from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^courses/(?P<teacher_id>[0-9]+)/$', views.courses, name='courses'),
    url(r'^lectures/(?P<course_id>[0-9]+)/$', views.lectures, name='lectures'),
]