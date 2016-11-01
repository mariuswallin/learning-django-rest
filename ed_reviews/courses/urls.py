from django.conf.urls import url

from . import views

# ulike linker root er hovedsiden for kurs
# neste link tar i mot en verdi som vi kan gjenbruke (link til spesifikk kurs)
# neste link viser rev basert paa course_pk id
# siste link tar i mot kurs id og spesifikk review id

urlpatterns = [
    url(r'^$', views.ListCreateCourse.as_view(), name='course_list'),
    url(r'(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyCourse.as_view(),
        name='course_detail'),
    url(r'^(?P<course_pk>\d+)/reviews/$',
        views.ListCreateReview.as_view(),
        name='review_list'),
    url(r'^(?P<course_pk>\d+)/reviews/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyReview.as_view(),
        name='review_detail'),
]