from django.db import models

"""CREATE TABLE posts (id=init primary key, title=varchar(100), description=varchar(400))"""
" all objects - Post.objects.all() ----> SELECT * FROM posts"
""" SELECT * FROM posts WHERE id=1"""
" one object - Post.objects.get(id=1) ----> SELECT * FROM posts WHERE id=1"
""" SELECT * FROM posts where title ILIKE '%a%'"""
" few items by condition - Post.objects.filter(title='title') ----> SELECT * FROM posts where title ILIKE '%a%'"
""" INSERT into posts (title, description) values ('title', 'description')"""
" create object - Post.object.create()"


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = None
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.description}"
