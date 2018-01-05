from django.contrib import admin

from .models import Task
from .models import Photo
from .models import Video

admin.site.register(Task)
admin.site.register(Photo)
admin.site.register(Video)
