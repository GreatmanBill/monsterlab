from django.conf.urls import patterns, include, url
from users import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monsterlab.views.home', name='home'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^message/', include('message.urls', namespace='message')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
