from django.contrib.auth.models import User
from django.db import models


class SearchResult(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200)
    searched_at = models.DateTimeField(auto_now=True)


class NewSearchResult(models.Model):
    user_name = models.ManyToManyField(User)
    keyword = models.CharField(max_length=200)
    searched_at = models.DateTimeField(auto_now=True)
