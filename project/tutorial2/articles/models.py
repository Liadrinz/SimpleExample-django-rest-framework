from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    owner=models.ForeignKey('auth.User',related_name='articles',on_delete=models.CASCADE,null=True,blank=True)
    
    class Meta:
        ordering = ('created',)