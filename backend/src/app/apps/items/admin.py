from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ("code", "name", "item_group", "progress_order", "item_type", "quantity")
    list_display = ("code", "name", "item_group", "item_type")
