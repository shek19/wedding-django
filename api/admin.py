from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Wedding)
admin.site.register(Guest)
admin.site.register(Checklist)
admin.site.register(BudgetItem)
admin.site.register(Vendor)
admin.site.register(WeddingVendor)