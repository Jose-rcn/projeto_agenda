from django.contrib import admin
from contact import models
# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','category')
    ordering = '-id',
#   list_filter = 'created_date'
    search_fields = 'id','first_name','last_name'
    list_per_page = 20
    list_display_links = 'id',
    list_editable = 'first_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id','name'
    ordering = '-id',
    list_display_links = 'id', 'name'