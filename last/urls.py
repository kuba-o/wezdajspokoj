from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import app.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'last.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', app.views.IndexView.as_view(), name='index'),
 )
urlpatterns += patterns('',
    (r'^(?P<path>.*)$', 'django.views.static.serve', ))
