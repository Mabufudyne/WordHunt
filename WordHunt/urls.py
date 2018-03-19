"""WordHunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from WordHuntApp import views
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',views.main, name='main'),
	url(r'^about/$',views.about, name='about'),
	url(r'^past/$',views.past, name='past'),
	url(r'^leaderboard/$',views.leaderboard, name='leaderboard'),
	url(r'^search/$',views.search, name='search'),
	url(r'^profile/stats/$',views.stats, name='stats'),
	url(r'^profile/current/$',views.current, name='current'),
	url(r'^profile/uploads/$',views.uploads, name='uploads'),
	url(r'^profile/settings/$',views.settings, name='settings'),
	url(r'^login/',views.user_login, name='login'),
	url(r'^register/',views.register, name='register'),
	url(r'^image/',views.image, name='image'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

]
