from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)


@admin.register(models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "contact_name", "email", "phone_number"]
    list_filter = ["name",  "contact_name", "phone_number"]
    search_fields = ["name", "category", "contact_name"]

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["brand", "category", "name", "quantity", "available", "created"]
    list_filter = ["brand", "category", "name", "quantity", "available"]
    search_fields = ["name", "category", "contact_name"]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ "first_name", "phone_number", "payment_status ", "delivery_status", "refund_requested", "refund_granted" ]
    list_filter = [ "first_name", "payment_status ", "delivery_status", "refund_requested", "refund_granted", "created" ]
    search_fields = [ "first_name", "last_name", "email", "phone_number" ]