from django.db import models

# Todo Model db table definition
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title



""" 
restful api
user endpoints:
- Get all users: /api/users
- Get single user: /api/users/<str:pk>
- Create user: /api/users/create
- Update user: /api/users/update/<str:pk>
- Delete user: /api/users/delete/<str:pk>
"""