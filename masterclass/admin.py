from django.contrib import admin
from masterclass.models import Masterclass




class MasterclassAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_mk','text_min','age_category','form','price','actuality')

admin.site.register(Masterclass, MasterclassAdmin)