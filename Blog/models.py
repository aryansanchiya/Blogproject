from django.db import models

# Create your models here.
class blogdetail(models.Model):
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100)
    date = models.DateField()
    content1 = models.TextField()
    image = models.ImageField(upload_to="media/pics")
    imagedetail = models.CharField(max_length=120)
    content2 = models.TextField()
    placeholder = models.URLField(max_length=200)
    category = models.CharField(max_length=100,default="") 

    def __str__(self):
        return self.heading 

class Comment(models.Model):
    post = models.ForeignKey(blogdetail,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    comment = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
class Projects(models.Model):
    projectname = models.CharField(max_length=255)
    projectlang = models.CharField(max_length=255)
    projectlink = models.URLField()