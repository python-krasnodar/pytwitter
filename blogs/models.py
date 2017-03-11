from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """
    This is a model representing a user's blog.
    """
    author = models.OneToOneField(User, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title + ' (Author: ' + self.get_author_name() + ')'

    def get_author_name(self):
        """
        This method will return the name of the author of the blog.

        Either his Name and Surname or username.

        :return:
        """
        if self.author.first_name != '' and self.author.last_name != '':
            return ' '.join([self.author.first_name, self.author.last_name])

        return self.author.username
