from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
	list_display_links = ('id', 'title')

# Register your models here.
admin.site.register(Listing, ListingAdmin)