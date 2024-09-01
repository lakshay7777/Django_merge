
# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# from blog.manager import usermanager
# from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from django.contrib.auth.models import User


# user = get_user_model()


class User(AbstractUser):
	  
	#   username = None
	phone_number = models.IntegerField(blank=True, null=True)
	email = models.EmailField(unique=True)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=250)
	country = models.CharField(max_length=250)
	user_profile_image = models.ImageField(upload_to='user',null=True, blank=True)

	#   USERNAME_FIELD = 'phone_number'
	#   REQUIRED_FIELDS = []
	#   objects = usermanager()
	def __str__(self):
		return self.username



class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = AutoSlugField(populate_from='name',null=True)

    def __str__(self):
        return self.name


###########{




class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = AutoSlugField(populate_from='name',null=True)
    def __str__(self):
        return self.name

###########}


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    ########{
    tag = models.ManyToManyField('Tag',null=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    thumnail_image  = models.ImageField(upload_to='thumnail_image', null=True,blank=True)
 
    #description = models.TextField(blank=True, null=True)
    ##########}
    feature_image  = models.ImageField(upload_to='feature_image', null=True,blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




   


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(blank=True)
    # location = models.CharField(max_length=100, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    user_profile_image = models.ImageField(upload_to='user', blank=True) 

def __str__(self):
        return self.user
	
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()




################cccccccccccccccccc}


class Comment(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(unique=False,blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    # created = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE,null=True )
    parent = models.ForeignKey('self', related_name="replies", on_delete=models.CASCADE,null=True)

    def _str_(self):
        if self.name:
            name = self.name
        else:
            name = self.text

        return  self.text
    


    


#class Comment(models.Model):
   # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    # other fields...

    