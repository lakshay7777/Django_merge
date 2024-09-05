from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


class User(AbstractUser):
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    user_profile_image = models.ImageField(upload_to='user')
   
    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=50,default='Uncategorized')
    slug = AutoSlugField(populate_from='name',)
   
   
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50,)
    slug = AutoSlugField(populate_from='name',)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    tag = models.ManyToManyField(Tag)
    slug = AutoSlugField(populate_from='title', unique=True,)
    thumnail_image = models.ImageField(upload_to='thumnail_image',)
    feature_image = models.ImageField(upload_to='feature_image',)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile_image = models.ImageField(upload_to='user',)
    
   
    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    name = models.CharField(max_length=255,)
    email = models.EmailField(unique=False,)
    text = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE,)
    parent = models.ForeignKey('self', related_name="replies", on_delete=models.CASCADE, null=True, blank=True)
    
   
    def __str__(self):
        if self.name:
            name = self.name
        else:
            name = self.text
        return self.text