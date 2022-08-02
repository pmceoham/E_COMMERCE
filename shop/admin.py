from django.contrib import admin
from .models import Catergory, Product
# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')


admin.site.register(Catergory, AdminCategory)
admin.site.register(Product, AdminProduct)
