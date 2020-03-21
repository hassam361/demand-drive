from django.contrib import admin
admin.site.site_header = "Demand Drive Admin"
admin.site.site_title = "Demand Drive Admin Portal"
admin.site.index_title = "Welcome to Demand Drive Admin Portal"
from .models import Demand,FulfillContent

admin.site.register(Demand)
admin.site.register(FulfillContent)
# Register your models here.
