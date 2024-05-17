from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.title

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    skype = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MyExpertise(models.Model):
    expertise = models.CharField(max_length=100)
    skills = models.CharField(max_length=150)

    def __str__(self):
        return self.expertise

class Skills(models.Model):
    skill = models.CharField(max_length=100)
    width = models.IntegerField(null=False)

    def __str__(self):
        return self.skill

class Languages(models.Model):
    language = models.CharField(max_length=40)
    grade = models.IntegerField(null=False)

    def __str__(self):
        return self.language

class Expertise(models.Model):
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    position = models.CharField(max_length=100, verbose_name="Position")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.position

class Education(models.Model):
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    place = models.CharField(max_length=100, verbose_name="Place")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.place

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email

