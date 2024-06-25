from django.contrib import admin

from .models import InventoryItem, Supplier

admin.site.register(InventoryItem)
admin.site.register(Supplier)
