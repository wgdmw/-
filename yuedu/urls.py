from django.conf.urls import url
from yuedu.views import IndexView,ListView,DetailView,TagsView

urlpatterns = [
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)', ListView.as_view(), name='list'),
    url(r'^tag/(?P<tag>[\s\S]*)/(?P<page>\d+)', TagsView.as_view(), name='tag'),
    url(r'^detail/(?P<art_id>\d+)',DetailView.as_view(),name='detail'),
    url(r'^',IndexView.as_view(),name='index'),
]
