from django.contrib import admin
from masterclass.models import Masterclass, Masterclass_events


class MasterclassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'category_mk','text_min','age_category','form','price','actuality',)
    list_editable = ( 'slug','category_mk','age_category','form','price','actuality',)
    list_filter = ('category_mk','age_category','form',)
    search_fields = ('title',)

class Masterclass_eventsAdmin(admin.ModelAdmin):
    list_display = ('MK', 'date', 'visiters_num',)
    list_editable = ( 'date', 'visiters_num',)
    list_filter = ('MK',)
    search_fields = ('MK',)


admin.site.register(Masterclass, MasterclassAdmin)

admin.site.register(Masterclass_events, Masterclass_eventsAdmin)