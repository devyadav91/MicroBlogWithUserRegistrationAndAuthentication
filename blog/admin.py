from django.contrib import admin
from .models import article

@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display = ['id','title','content']