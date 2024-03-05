from django.contrib import admin

# Register your models here.

from django.contrib import admin
from Blog.models import blogdetail,Comment,Projects

admin.site.site_header = 'Blog App'

class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","created_on")
admin.site.register(Comment, CommentAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("projectname","projectlink")
admin.site.register(Projects,ProjectsAdmin)

class blogdetailAdmin(admin.ModelAdmin):
    list_display = ("heading","date","category")
    list_filter = ("date","heading")

admin.site.register(blogdetail,blogdetailAdmin)
