from django.contrib import admin
from .models import House,WareHouse,Land
# Register your models here.

#house admin
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    model=House
    fields=['name','location','price','bedrooms','bathrooms','toilets','dealer','image1']
    list_display=['name','location','price','dealer']
    list_filter=['date_added']


@admin.register(WareHouse)
class WareHouseAdmin(admin.ModelAdmin):
    model=WareHouse
    fields=['name','location','price','dealer','space']
    list_display=['name','location','space','price','dealer']
    list_filter=['date_added']

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    model=Land
    fields=['name','location','space','price','dealer']
    list_display=['name','location','price','dealer','space']
    list_filter=['date_added']

