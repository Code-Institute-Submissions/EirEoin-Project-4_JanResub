import unittest
from django.test import TestCase
from .models import Comment, Post

class CommentModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", body="Test post body.")
        self.comment = Comment.objects.create(
            post=self.post,
            name="Test User",
            email="testuser@example.com",
            body="Test comment body.",
            approved=True
        )

    def test_str_representation(self):
        self.assertEqual(str(self.comment), "Comment Test comment body. by Test User")

    def test_post_relationship(self):
        self.assertEqual(self.comment.post, self.post)

    def test_approved_default(self):
        comment = Comment.objects.create(
            post=self.post,
            name="Test User 2",
            email="testuser2@example.com",
            body="Test comment body 2."
        )
        self.assertFalse(comment.approved)

    def test_ordering(self):
        comment2 = Comment.objects.create(
            post=self.post,
            name="Test User 2",
            email="testuser2@example.com",
            body="Test comment body 2.",
            approved=True
        )
        self.assertEqual(list(Comment.objects.all()), [self.comment, comment2])