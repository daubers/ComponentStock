from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ComponentStock.views.home', name='home'),
    # url(r'^ComponentStock/', include('ComponentStock.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stock/view/', 'Stock.views.stock'),
    url(r'^component/view/', 'Components.views.viewComponents'),
    url(r'^component/get/(?P<dataTable>\w{0,50})/$', 'Components.views.getComponents'),
    url(r'^component/add/form/', 'Components.views.newComponentForm'),
    url(r'^component/add/', 'Components.views.newComponent'),
    url(r'^supplier/add/form/', 'Components.views.newSupplierForm'),
    url(r'^supplier/add/', 'Components.views.newSupplier'),
    url(r'^supplier/get/', 'Components.views.getSuppliers'),
    url(r'^manufacturer/add/form/', 'Components.views.newManufacturerForm'),
    url(r'^manufacturer/add/', 'Components.views.newManufacturer'),
    url(r'^manufacturer/get/', 'Components.views.getManufacturer'),
    url(r'^project/add/form/', 'CompProjects.views.addForm'),
    url(r'^project/add/', 'CompProjects.views.addProject'),
)
