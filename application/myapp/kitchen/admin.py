from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(ItemModel)
admin.site.register(MonthlyList)


class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(Contact,ContactAdmin)