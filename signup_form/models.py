from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(db_index=True, auto_now_add=True)

# Create your models here.
class Volunteer(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, db_index=True)
    interests = models.ManyToManyField('Interest', related_name='interests', blank=True)
    def __str__(self):
        return '%s' % self.name

class Interest(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    experts = models.ManyToManyField(User)

    def __str__(self):
        return '%s' % self.title
