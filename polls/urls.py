from django.conf.urls import patterns, url, include
from django.conf import settings

from polls import evernote_demo
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
    url(r'^get_articles/$', views.get_articles, name='get_articles'),
    url(r'^search_scholar/$', views.search_scholar, name='search_scholar'),
    url(r'^test_threejs/$', views.test_threejs, name='test_threejs'),
    url(r'^test_threejs2/$', views.test_threejs2, name='test_threejs2'),
    url(r'^test_3d_editor/$', views.test_3d_editor, name='test_3d_editor'),
    url(r'^test_import_json/$', views.test_import_json, name='test_import_json'),
    url(r'romania/$', views.romania, name='romania'),
    url(r'human/$', views.human, name='human'),

    # Smarter Doctor / Evernote prototyping.
    url(r'^show_notes/$', views.show_notes, name='show_notes'),
    url(r'^show_evernotes/$', evernote_demo.show_evernotes, name='show_evernotes'),
    url(r'^show_evernote_timeline/$', evernote_demo.evernote_timeline_page, name='evernote_timeline_page'),
    url(r'^_/get_evernote_timeline_data/$', evernote_demo.get_evernote_timeline_data, name='get_evernote_timeline_data'),
)
