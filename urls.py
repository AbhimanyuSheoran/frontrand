from django.conf.urls import patterns, include, url
import settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
                        url(r'^admin/','adminapp.views.admin', name='admin'),
                        url(r'^show/$', 'adminapp.views.picture_upload', name='show'),
                        url(r'^delete/$', 'adminapp.views.delete_picture', name='del'),
                        url(r'^stat-change/', 'adminapp.views.index', name='stat'),
                        url(r'^$', TemplateView.as_view(template_name="home.html")),
                        url(r'^faces/$', 'adminapp.views.faces', name='faces'),
                        url(r'^delete-face/$', 'adminapp.views.delete_face', name='del_Face'),
                        url(r'^edit-face/$', 'adminapp.views.edit_face', name='edit_Face'),
                        )
# handler403 = 'adminapp.views.error403'
# handler404 = 'adminapp.views.error404'


