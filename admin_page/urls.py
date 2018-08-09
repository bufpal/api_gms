from django.urls import re_path
from . import views

app_name = 'admin-page'

urlpatterns = [
    re_path(r'^$', views.root_page, name='root'),
    re_path(r'^users/$', views.profile_list, name='profile-list'),
    re_path(r'^users/(?P<pk>\d+)/$', views.profile_detail, name='profile-detail'),

    re_path(r'^inquiry/$', views.inquiry_list, name='inquiry-list'),
    re_path(r'^inquiry/(?P<pk>\d+)/$', views.inquriy_detail, name='inquiry-detail'),

    re_path(r'^notice/$', views.notice_list, name='notice-list'),
    re_path(r'^notice/(?P<pk>\d+)/$', views.notice_detail, name='notice-detail'),
    re_path(r'^notice/new$', views.notice_new, name='notice-new'),
]