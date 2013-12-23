# This also imports the include function
from django.conf.urls.defaults import *
from django.conf import settings

from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^resources/(?P<path>.*)$',
      'django.views.static.serve',
      { 'document_root': settings.MEDIA_ROOT } ),
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)
