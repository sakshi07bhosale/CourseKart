from django.urls import path
from .views import index,courses,about,contact
from . import views

urlpatterns = [
   path('',index, name="index"),
   path('courses/',courses, name="courses"),
   path('about/',about, name="about"),
   path('contact/',contact, name="contact"),
   #  path('', views.course_list, name='course_list'),
    path('detail/<int:id>/', views.course_detail, name='course_detail'),
]