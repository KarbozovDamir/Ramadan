from django.contrib import admin

from .models import *

# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'time_create')
#     list_display_links = ('id', 'title')
    # search_fields = ('title', 'content')
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {"slug": ("title",)}
    # fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    # readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    # save_on_top = True


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     prepopulated_fields = {"slug": ("name",)}

admin.site.register(Answer)
admin.site.register(Category)


# admin.site.register(Answer, AnswerAdmin)
# admin.site.register(Category, CategoryAdmin)