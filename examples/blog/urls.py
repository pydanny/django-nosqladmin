from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^nosqladmin/', include('nosqladmin.urls')),
    url(r'^', include('articles.urls')),    
)
