from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('gallery/', views.gallery, name='gallery'),
    path('course-detail/', views.courseDetail, name='coursedetail'),
    
]
