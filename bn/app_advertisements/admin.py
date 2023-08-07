from django.contrib import admin
from .models import Advertisements
# Register your models here.

class Adveradmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description',
                    'price', 'createdat', 'updateat',
                    'auction','image']
    list_filter = ['auction', 'createdat']

    actions = ['make_auction_as_false']

    fieldsets = (
        ('Общее',{
            'fields': ('title', 'description','image',
                       'user'),
        }),
        ('Финансы',{
            'fields': ('price','auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Delete auction')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)






admin.site.register(Advertisements, Adveradmin)
