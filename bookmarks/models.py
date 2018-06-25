from django.db import models
from uuid import uuid4

class Bookmark(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=200)
  url = models.URLField(unique=True)
