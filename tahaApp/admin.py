from django.contrib import admin
from .models import *


class TahaAppAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Shop


admin.site.register(Shop)
admin.site.register(Affiliate)
admin.site.register(Product)
admin.site.register(Receipt)