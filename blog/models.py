from django.db import models

from django_ckeditor_5.fields import CKEditor5Field

from user.models import User


class PostCategory(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    thumbnail = models.ImageField(upload_to='posts/thumbnails/')
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE, related_name='posts_by_category')
    title = models.CharField(max_length=255, unique=True)
    short_desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = CKEditor5Field()


    def __str__(self):
        return f"""ID: {self.id} | Title: {self.title}"""

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class PostTag(models.Model):
    title = models.CharField(max_length=255)
    post = models.ManyToManyField(to=Post, related_name='tags_of_post')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post Tag'
        verbose_name_plural = 'Post Tags'


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # Связь с моделью Post
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Post Comments"
        ordering = ['-created_at']


