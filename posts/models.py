from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save

from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    # slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True) # will be set only one time

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("posts:update", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     slug = slugify(instance.title)
#     qs = Post.objects.filter(slug=slug)
#     exists = qs.exists()
#     if exists:
#         slug = "%s-%s" %(slug, qs.first().id)
#     instance.slug = slug
    # if not instance.slug:
    #     instance.slug = create_slug(instance)

# pre_save.connect(pre_save_post_receiver, sender=Post)
