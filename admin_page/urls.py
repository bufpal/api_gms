from django.conf import settings
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'admin-page'

urlpatterns = [
    path('', views.root_page, name='admin-root'),
    re_path(r'^users/$', views.profile_list, name='profile-list'),
    re_path(r'^users/(?P<pk>\d+)/$', views.profile_detail, name='profile-detail'),

    re_path(r'^inquiry/$', views.inquiry_list, name='inquiry-list'),
    re_path(r'^inquiry/(?P<pk>\d+)/$', views.inquriy_detail, name='inquiry-detail'),

    re_path(r'^notice/$', views.notice_list, name='notice-list'),
    re_path(r'^notice/(?P<pk>\d+)/$', views.notice_detail, name='notice-detail'),
    re_path(r'^notice/new$', views.notice_new, name='notice-new'),

    path('login/', auth_views.LoginView.as_view(template_name='admin_page/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
