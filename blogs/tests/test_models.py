from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Blog


class BlogTestCase(TestCase):
    def test_taking_the_name_of_the_author(self):
        author = User.objects.create(username="test")
        blog = Blog.objects.create(author=author, title="Test's blog")

        self.assertEqual(blog.get_author_name(), author.username)

    def test_taking_the_name_of_the_author_with_full_name(self):
        author = User.objects.create(username="test", first_name="Test", last_name="Tester")
        blog = Blog.objects.create(author=author, title="Test's blog")

        self.assertEqual(blog.get_author_name(), ' '.join([author.first_name, author.last_name]))
