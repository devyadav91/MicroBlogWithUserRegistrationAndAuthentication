from django.db import models
from django.contrib.auth import get_user_model
# from django.conf import settings
# from django.contrib.auth.models import User

def logged_user(request):
    current_user=request.user
    return request.user.id
User = get_user_model()

class article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1250)
    author = models.CharField(max_length=50)
