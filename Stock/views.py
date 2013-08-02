from models import Supplier,Component,PurchaseOrder,Stock
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def stock(request):
    """
        Shows the current stock of components
    """
    stock_items = get_object_or_404(Stock)
