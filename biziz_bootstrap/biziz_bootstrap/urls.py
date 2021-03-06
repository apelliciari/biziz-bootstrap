from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('frontend.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^skeleton/$', 'skeleton', name='skeleton'),
    url(r'^azienda/(?P<parametro>[^/]+)/$', 'azienda', name="azienda"),
    url(r'^news/(?P<parametro>[^/]+)/$', 'news', name="news"),
    # url(r'^biziz_bootstrap/', include('biziz_bootstrap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
