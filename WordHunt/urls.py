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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from WordHuntApp import views
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.main, name='main'),
    url(r'^about/$',views.about, name='about'),
    url(r'^past/$',views.past, name='past'),
    url(r'^leaderboard/all_time/$',views.leaderboard, name='leaderboard'),
    url(r'^leaderboard/current/$',views.current_leaderboard, name='current_leaderboard'),
    url(r'^search/users/$',views.search, name='search'),
	url(r'^search/words/$',views.words_search, name='words_search'),
    url(r'^profile/stats/(?P<username>[\w\-]+)/$',views.stats, name='stats'),
    url(r'^profile/current/(?P<username>[\w\-]+)/$',views.current, name='current'),
    url(r'^profile/uploads/(?P<username>[\w\-]+)/$',views.uploads, name='uploads'),
    url(r'^profile/settings/(?P<username>[\w\-]+)/$',views.settings, name='settings'),
    url(r'^login/$',views.user_login, name='login'),
    url(r'^register/$',views.register, name='register'),
    url(r'^word/(?P<username>[\w\-]+)/(?P<word>[\w\-]+)/$', views.word, name='word'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
url(r'^all/(?P<word>[\w\-]+)/$',views.all, name='all'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
