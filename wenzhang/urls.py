from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^search', include('haystack.urls')),
    url(r'^',include('yuedu.urls',namespace='index')),

]
