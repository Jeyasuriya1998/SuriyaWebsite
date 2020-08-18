from django.db import models

# Create your models here.
class Achievements(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200)
    thumbnil = models.ImageField(null=True, blank=True, upload_to='images')

    body = models.TextField()
    pdf = models.FileField(upload_to="pdf", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    feature = models.BooleanField(default=False)
    
    def __str__(self):
        return self.headline
    
class Projects(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200)
    thumbnil = models.ImageField(null=True, blank=True, upload_to="images")
    body = models.TextField()
    link = models.URLField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    feature = models.BooleanField(default=False)
    
    def __str__(self):
        return self.headline
    