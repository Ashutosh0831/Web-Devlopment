from django.db import models

# Create your models here.
class first(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    Website = models.URLField(max_length=200)
    description = models.TextField()
   # def __str__(self):
   #     return f"{self.name} - {self.email} - {self.phone} - {self.Website}"
        

class report_data(models.Model):
    status_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    Course = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='images/', blank=True, null=True,max_length=250)
    status = models.CharField(max_length=100, default="Pending")


class register_data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)


class login_data(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    