from django.contrib import admin
from cars.models import CarModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['company', 'model', 'speed', 'created_at']
    search_fields = ['model']
    list_filter = ['created_at', 'company']
