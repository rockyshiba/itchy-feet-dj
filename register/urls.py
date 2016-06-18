from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.travellers, name='travellers'), #domain.com/travellers
    url(r'^(?P<traveller_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^register/$', views.register, name='register'),
]