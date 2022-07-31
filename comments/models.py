from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
class CommentingUser(models.Model):
	name = models.CharField(max_length=40)
	
	def __str__(self):
		return self.name

class Comment(models.Model):
    author = models.ForeignKey(CommentingUser,
	on_delete = models.CASCADE,)
    body  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self' , null=True, blank= True, on_delete=models.CASCADE, related_name='replies')
	
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.author) + str(self.body)
        

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
                return True
        return False

