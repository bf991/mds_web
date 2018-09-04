from django.contrib import admin
from clothes.models import Clothe, Bijou

class ClotheAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','type','text_min','age_category','male','price','actuality',)
    list_editable = ('slug','type','age_category','male','price','actuality',)
    list_filter = ('type', 'male','age_category',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class BijouAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','type','text_min','price','actuality',)
    list_editable = ('slug','type','price','actuality',)
    list_filter = ('type',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Clothe, ClotheAdmin)
admin.site.register(Bijou, BijouAdmin)

