from django.contrib import admin
from .models import Project
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["project_title", "project_published"]}),
        ("URL", {"fields": ["project_url"]}),
        ("Content", {"fields": ["project_content"]}),
        ("Image", {"fields":["project_image"]}),
        ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Project, ProjectAdmin)