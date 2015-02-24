from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import patterns, url


from . import views
from django.shortcuts import redirect


urlpatterns = patterns('',
    url(r'^register-computer/(?P<label>.+)/$', 'technicians.views.register_computer_installation', name='register_computer_installation'),
    url(r'^computer/login/(?P<label>[\w\d]+)/(?P<user>\w+)/$', 'technicians.views.computer_login', name='computer_login'),
    url(r'^computer/logout/(?P<label>[\w\d]+)/(?P<user>\w+)/$', 'technicians.views.computer_logout', name='computer_logout'),
    url(r'^computer/$', views.ComputerList.as_view(), name='computer_list'),
    url(r'^computer/(?P<pk>\d+)/log/$', views.ComputerLog.as_view(), name='computer_log'),
    url(r'^computer/(?P<pk>\d+)/log/create/$', views.ComputerLogAdd.as_view(), name='computer_log_add'),
    url(r'^/?$', lambda x: redirect('technicians:computer_list'),)
)
