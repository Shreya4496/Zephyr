"""Zephyr URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from Homepage.views import *
from Zephyr.views import *

from trend_promotion.views import abc, potList, nonVUser, get_tweets
from local_promo.views import local_trends

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homepage/$', HomePage, name='homepage'),
url(r'^dashboard/$', DashBoard, name='homepage'),

#url(r'^trend_promotion/',abc),
#url(r'^trend_promotion/',include('trend_promotion.urls',namespace="trend_promotion")),
url(r'^trend_promotion/',abc),
url(r'^tweets/',get_tweets),

url(r'^local_trendpromo/', local_trends),
url(r'^potential_offers/', potList),
url(r'^nonVUser/', nonVUser),
url(r'^offers/$', Offers, name='offers'),

url(r'^trips_all/$', trips_all, name='trips_all'),
   # url(r'^realtime_feedback/$', newUpdate, name='preferences'),

url(r'^profile/$', Profile, name='offers'),

url(r'^login/$', Login, name='login'),
url(r'^register/$', register, name='register'),
url(r'^logout/$', Logout, name='logout'),


#url(r'^offers/$', Offers, name='offers'),

]
