from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)  # Make sure 'created_at' is defined in the model
    list_display = ('id', 'user', 'content_type', 'created_at')  # Ensure the field exists
    list_filter = ('content_type', 'created_at')  # Add fields that exist in the model

admin.site.register(Content, ContentAdmin)