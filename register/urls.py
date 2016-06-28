from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'), #domain.com/
    url(r'^travellers/(?P<traveller_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^travellers/$', views.travellers, name='travellers'),
    url(r'^about/$', views.about, name='about'),
]