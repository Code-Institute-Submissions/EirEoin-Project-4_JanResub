from django.test import TestCase
from .models import Tag, TagSubject, Post

class TagTest(TestCase):
    def setUp(self):
        # Create test data
        self.subject = TagSubject.objects.create(name="Test Subject")
        self.post1 = Post.objects.create(title="Test Post 1")
        self.post2 = Post.objects.create(title="Test Post 2")
        self.tag = Tag.objects.create(
            title="Test Tag",
            subject=self.subject,
            articles=[self.post1, self.post2]
        )

    def test_title_field(self):
        # Test that the title field is a CharField with a maximum length of 200 and is unique
        self.assertEqual(self.tag._meta.get_field("title").max_length, 200)
        self.assertTrue(self.tag._meta.get_field("title").unique)

    def test_subject_field(self):
        # Test that the subject field is a ForeignKey to the TagSubject model and that the on_delete behavior is set to CASCADE
        self.assertEqual(self.tag._meta.get_field("subject").related_model, TagSubject)
        self.assertEqual(self.tag._meta.get_field("subject").on_delete.__name__, 'CASCADE')
        self.assertEqual(self.tag._meta.get_field("subject").related_query_name, 'tags')

    def test_articles_field(self):
        # Test that the articles field is a ManyToManyField to the Post model and that the related_name is "tags"
        self.assertEqual(self.tag._meta.get_field("articles").related_model, Post)
        self.assertEqual(self.tag._meta.get_field("articles").related_name, 'tags')

    def test_str_method(self):
        # Test that the __str__ method returns the correct string
        self.assertEqual(str(self.tag), "Test Tag (Articles: 2)")

    def test_article_count_method(self):
        # Test that the article_count method returns the correct number of articles
        self.assertEqual(self.tag.article_count(), 2)