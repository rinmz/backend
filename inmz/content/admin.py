from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_type', 'created_at')
    list_filter = ('content_type', 'created_at')
    search_fields = ('user__username', 'content')
    readonly_fields = ('created_at',)