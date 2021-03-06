from django.conf.urls import include, url
from django.contrib import admin
from todolist.views import todo_list, complete, delete


urlpatterns = [
    # Examples:
    # url(r'^$', 'todolist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', todo_list),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^complete/(?P<pk>\d+)/', complete),
    url(r'^delete/(?P<pk>\d+)/', delete),
]
