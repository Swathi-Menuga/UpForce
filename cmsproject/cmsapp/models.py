from django.db import models

# Create your models here.
# 1.  The database should contain three tables named User, Post/Blog, and Like.

# 2. The User table should store user information such as user ID, name, email, password, 
#     and other relevant details.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
# 3. The Post/Blog table should store post/blog information such as post ID, title, description,
#     content, creation date, and other relevant details.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

# 4. The Like table should store information about the likes of each post/blog, such as like ID,
#    post ID, user ID, and other relevant details.    

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


