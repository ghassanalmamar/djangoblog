from django.contrib import admin
from myblog.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    empty_value_display = ''
    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = ''
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

