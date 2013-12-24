from django.conf.urls import patterns, url, include
from django.conf import settings

from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^search-results/$', views.search_results, name='search_results'),                
    url(r'^claim/$', views.claim, name='claim'),
    url(r'^submit_article/$', views.submit_article, name='submit_article'),
    url(r'^convert_text/$', views.convert_text, name='convert_text'),
    url(r'^convert_text2/$', views.convert_text2, name='convert_text2'),
    url(r'^smart/$', views.smart, name='smart'),
    url(r'^smart2/$', views.smart2, name='smart2'),
    url(r'^show_notes/$', views.show_notes, name='show_notes'),
)
