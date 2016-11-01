from django.conf.urls import url

from . import views

# as_view brukes naar det ikke rutes videre

urlpatterns = [
    url(r'^$', views.ListCreateCourse.as_view(), name='course_list'),
]