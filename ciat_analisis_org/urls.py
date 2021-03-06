from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from analisis.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ciat_analisis_org.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^$', IndexView.as_view()),
)
