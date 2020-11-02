from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Keep draft and pubished posts separate
STATUS = (
	(0,"Draft"),
	(1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Stores metadata
    class Meta:
        ordering = ['-created_on']

    # Default human-readable representation of object
    def __str__(self):
        return self.title

class Comment(models.Model):
    # foreign key relationship: establishes many-to-one relationship with Post model
    # related_name attribute names the attributes for the foreign key relationship
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    # accept commenter name and email and comment body
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    # sort results in descending order by default
    created_on = models.DateTimeField(auto_now_add=True)

    # manually allow all the comments posted to prevent spam
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    # default human-readable representation of the object
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
