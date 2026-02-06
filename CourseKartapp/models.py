from django.db import models

# Create your models here.
class ContactData(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "ContactData"
   