from django.contrib import admin
from masterclass.models import Masterclass





class MasterclassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'category_mk','text_min','age_category','form','price','actuality',)
    list_editable = ( 'slug','category_mk','age_category','form','price','actuality',)
    list_filter = ('category_mk','age_category','form',)
    search_fields = ('title',)



admin.site.register(Masterclass, MasterclassAdmin)