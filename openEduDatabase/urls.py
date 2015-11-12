from . import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'lectures', views.LectureViewSet)
router.register(r'breakpoints', views.BreakpointViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'breakpointscore', views.BreakpointScoreViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]