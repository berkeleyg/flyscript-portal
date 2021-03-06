# Copyright (c) 2013 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the 
# MIT License set forth at:
#   https://github.com/riverbed/flyscript-portal/blob/master/LICENSE ("License").  
# This software is distributed "AS IS" as set forth in the License.


from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',

    url(r'^ipaddr/(?P<addr>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)$', 'apps.geolocation.views.getIPAddress'),
    url(r'^location/(?P<name>.+)$', 'apps.geolocation.views.getLocation')
    )
