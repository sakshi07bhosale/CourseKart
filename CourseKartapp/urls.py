from django.urls import path
from .views import index,courses,about,contact
urlpatterns = [
   path('',index, name="index"),
   path('courses/',courses, name="courses"),
   path('about/',about, name="about"),
   path('contact/',contact, name="contact"),
]
