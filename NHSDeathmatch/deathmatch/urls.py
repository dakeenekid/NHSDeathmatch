from django.conf.urls import url
from deathmatch import views


urlpatterns = [
    url(r'^$', views.view_home, name='home'),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]