from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog


class Feed(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title + ' - ' + self.user.username
