from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post (models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    feautured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_likes', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def tag_titles(self):
        return ', '.join([a.title for a in self.tags.all()])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class TagSubject (models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.title}"


class Tag (models.Model):
    title = models.CharField(max_length=200, unique=True, blank=True)
    subject = models.ForeignKey(TagSubject, on_delete=models.CASCADE, blank=True, null=True, related_query_name="tags")
    articles = models.ManyToManyField(Post, related_name="tags", blank=True)

    def __str__(self):
        return f"{self.title} (Articles: {self.article_count()})"

    def article_count(self):
        return self.articles.count()
