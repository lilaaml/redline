from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'price_per_month', 'list_date', 'realtor')
    list_display_links = ('id', 'name')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('name', 'sub_district', 'location', 'floor_view', 'unit_type', 'condition', 'price_per_month', 'price_per_year', 'facility')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
