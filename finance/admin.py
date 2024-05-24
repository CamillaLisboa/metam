from django.contrib import admin
from .models import Person, Bill

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']
    list_display = ['name', 'doc','income']

admin.site.register(Person, PersonAdmin)


class BillAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name', 'due_date']
    list_display = ['name', 'price','due_date']

admin.site.register(Bill, BillAdmin)