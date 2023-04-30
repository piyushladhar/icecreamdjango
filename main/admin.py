from django.contrib import admin
from .models import Products,Users,Orders
# Register your models here.
admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Orders)