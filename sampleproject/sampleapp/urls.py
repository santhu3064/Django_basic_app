from django.conf.urls import url

from sampleapp import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]