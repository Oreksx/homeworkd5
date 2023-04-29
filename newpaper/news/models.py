from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    ratingAuthor = models.IntegerField(default = 0)

    def update_rating(self):
        postrating = self.post_set.all().aggregate(allpost=Sum('ratingpost'))
        prat = 0
        prat += postrating.get('allpost')
        commentrate = self.user.comment_set.all().aggregate(allcomment=Sum('ratingcomment'))
        crat = 0
        crat += commentrate.get('allcomment')
        self.ratingAuthor = prat * 3 + crat
        self.save()

class Category(models.Model):
    categoryname = models.CharField(max_length = 64, unique = True)

class Post(models.Model):
    POST = 'PO'
    NEWS = 'NE'
    TYPE_IN_PLACE = [
        (POST, 'post'),
        (NEWS, 'news'),
    ]
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    typepost = models.CharField(max_length = 2, choices = TYPE_IN_PLACE, default = POST)
    datepost = models.DateTimeField(auto_now_add = True)
    posts = models.ManyToManyField(Category, through = 'PostCategory')
    titlepost = models.CharField(max_length = 64, default = 'title')
    textpost = models.TextField()
    ratingpost = models.IntegerField(default = 0)

    def like(self):
        self.ratingpost += 1
        self.save()
    
    def dislike(self):
        self.ratingpost -= 1
        self.save()
    
    def preview(self):
        return self.textpost[0:123] + '...'
    
    def get_absolute_url(self):
        return f'/news/{self.id}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    textcomment = models.TextField()
    datecomment = models.DateTimeField(auto_now_add = True)
    ratingcomment = models.IntegerField(default = 0)

    def like(self):
        self.ratingcomment += 1
        self.save()

    def dislike(self):
        self.ratingcomment -= 1
        self.save()
    
    def __str__(self):
        try:
            return self.post.author.user.username
        except:
            return self.user.username









