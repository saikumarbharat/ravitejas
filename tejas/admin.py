from django.contrib import admin
from .models import Post,Comment,ResearchPaper,Publisher,Author,Project

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'technology' )
    #fields = ['emp_name', ('emp_designation')]
# Register the admin class with the associated model
admin.site.register(Project, ProjectAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Publisher)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth' )
    #fields = ['emp_name', ('emp_designation')]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'isbn')
from django.contrib import admin

# Register your models here.
