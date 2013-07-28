from django.contrib import admin
from models import Stock, PurchaseOrder, PurchaseOrderToComponent

admin.site.register(Stock)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderToComponent)