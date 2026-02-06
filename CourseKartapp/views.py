from django.shortcuts import render,redirect
from .models import ContactData

# Create your views here.
def index(request):
    return render(request, 'CourseKartapp/index.html')

def courses(request):
    return render(request, 'CourseKartapp/courses.html')

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
