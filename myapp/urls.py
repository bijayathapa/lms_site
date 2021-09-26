from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('course/', views.course, name='course'),
    path('gallery/', views.gallery, name='gallery'),
    path('course-detail/', views.courseDetail, name='coursedetail'),

    #path('social/',views.books_list, name='social'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('uploadcourse/', views.uploadCourse, name = 'uploadcourse'),
    path('writeblog/', views.writeBlog, name='writeblog'),
    
]
