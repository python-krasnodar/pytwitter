from django.db import models
from blogs.models import Blog


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' (Author: ' + self.get_author_name() + ')'

    def get_author_name(self):
        return self.blog.get_author_name()
