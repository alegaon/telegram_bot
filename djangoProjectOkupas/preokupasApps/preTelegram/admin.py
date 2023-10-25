from django.contrib import admin
from preTelegram.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']