from django.conf.urls import patterns, url

urlpatterns = patterns('multipart_form_data.views',
    url(r'^upload_form/$', 'upload_form'),
    url(r'^upload_serializers/$', 'upload_serializers'),
)