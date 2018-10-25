from django.contrib import admin
from news.models import News, Category, Tag

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','category','text_min','description','keyword',)
    list_editable = ( 'slug','category','description','keyword',)
    list_filter = ('category',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_editable = ( 'slug',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
