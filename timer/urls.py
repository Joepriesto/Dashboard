from django.conf.urls import url

from . import views

app_name = 'timer'
urlpatterns = [
	url(r'^$',views.IndexView.as_view(), name='index'),
# ex:/timer/batch/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name ='detail'),

	url(r'^(?P<lot_number>[0-9]+)/start/$', views.start, name ='start'),

	url(r'^(?P<pk>[0-9]+)/running/$', views.RunningView.as_view(), name='running')



]
