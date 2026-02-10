from django.db import models

# Create your models here.
class ContactData(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "ContactData"
   
#    =====================
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="No Description")
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    duration_months = models.IntegerField(default=0)
    level = models.CharField(max_length=50, default="Beginner")
    price = models.IntegerField()
    preview_video_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
