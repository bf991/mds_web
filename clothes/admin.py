from django.contrib import admin
from clothes.models import Clothe, Bijou

class ClotheAdmin(admin.ModelAdmin):
    list_display = ('title', 'type','text_min','age_category','male','price','actuality')

class BijouAdmin(admin.ModelAdmin):
    list_display = ('title', 'type','text_min','price','actuality')

admin.site.register(Clothe, ClotheAdmin)
admin.site.register(Bijou, BijouAdmin)

