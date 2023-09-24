from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

class PostsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="salih@mail.com",
            password="testpass",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content",
        )
    def test_post_model(self):
        post = self.post
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.title, "A good title")
        self.assertEqual(post.body, "Nice body content")


