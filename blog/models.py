from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        """to filter out and retrieve only published """
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)  
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    # on CASCADE when delete  user deletes all his posts, maybe not the best option
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # Default manager
    postobjects = PostObjects()  # Custom manager

    class Meta:
        ordering = ("-published",)
    
    def __str__(self):
        return self.title
    
