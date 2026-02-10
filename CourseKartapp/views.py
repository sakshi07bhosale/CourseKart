from django.shortcuts import render,redirect, get_object_or_404
from .models import ContactData,Course

# Create your views here.
def index(request):
    return render(request, 'CourseKartapp/index.html')

def courses(request):
    courses = Course.objects.all()
    return render(request, 'CourseKartapp/courses.html', {'courses': courses})

def about(request):
    return render(request, 'CourseKartapp/about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        ContactData.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect("contact")
    return render(request, 'CourseKartapp/contact.html')



# ================================
# Show all courses
# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'CourseKartapp/courses.html', {'courses': courses})


# Separate page for one course
def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', {'course': course})    