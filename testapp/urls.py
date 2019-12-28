from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import index, guest, available, invoices, check_data, post_invoice, edit, delete_data, change_invoice, check_data
from testapp import urls


urlpatterns = [
    url(r'^accessed/available/delete/(?P<param>\d+)/$', delete_data, name="delete_data"),
    url(r'^accessed/available/$', available, name='available'),
    url(r'^accessed/available/edit/(?P<param>\d+)/change_invoice/$', change_invoice, name="change_invoice"),
    url(r'^accessed/available/edit/(?P<param>\d+)/$', edit, name="edit"),
    url(r'^accessed/available/edit/(?P<param>\d+)/check_data/$', check_data, name='check_data'),
    url(r'guest/', guest, name='guest_page'),
    url(r'^invoices/$', invoices, name='invoices_page'),
    url(r'^invoices/check_data/$', check_data, name='check_data'),
    url(r'^post_invoice/$', post_invoice, name='post_invoice'),
    url('^$', index, name='homepage'),
]