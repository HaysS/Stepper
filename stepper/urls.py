"""stepper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from habit_lists import views as habit_lists_views

urlpatterns = [
    	url(r'^$', habit_lists_views.home_page, name='home'),
	url(r'^habit_lists/new', habit_lists_views.new_habit_list, name='new_habit_list'),
	url(r'^habit_lists/(\d+)/$', habit_lists_views.view_habit_list, name='view_list'),
	url(r'^habit_lists/(\d+)/add_habit$', habit_lists_views.add_habit, name='add_habit'),
	#url(r'^admin/', include(admin.site.urls)),
]
