from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'CourseKartapp/index.html')

def courses(request):
    return render(request, 'CourseKartapp/courses.html')

def about(request):
    return render(request, 'CourseKartapp/about.html')
def contact(request):
    return render(request, 'CourseKartapp/contact.html')
