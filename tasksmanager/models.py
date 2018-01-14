from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Task(models.Model):
    # id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tasks_assigned', verbose_name='assigned to')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Photo(models.Model):
    task = models.ForeignKey(Task, blank=True, null=True, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images', verbose_name='Ссылка картинки')

    def publish(self):
        self.save()

    #def __str__(self):
        #return self.image


class Video(models.Model):
    videokey = models.ForeignKey(Task, blank=True, null=True, default=None, related_name='videos', on_delete=models.CASCADE)
    video = models.CharField(blank=True, max_length=300)

    def publish(self):
        self.save()

    def __str__(self):
        return self.video
