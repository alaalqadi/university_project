from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^add_post/$', views.add_edit_post, name='add_post'),
    url(r'^edit_post/(\d+)/$', views.add_edit_post, name='edit_post'),
    url(r'^delete_post/(\d+)/$', views.delete_post, name='delete_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
