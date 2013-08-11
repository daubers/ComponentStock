from models import Supplier,Component,PurchaseOrder,Stock
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context


def stock(request):
    """
        Shows the current stock of components
    """
    stock_items = get_object_or_404(Stock)
    t = get_template('Stock/stock_index.html')
    html = t.render(Context({'Stock': stock_items}))
    return HttpResponse(html)