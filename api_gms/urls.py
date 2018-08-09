from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),
    re_path(r'^api/v1/', include('v1.urls', namespace='v1')),
    re_path(r'^admin-page/', include('admin_page.urls', namespace='admin-page')),
    
    re_path(r'^api-jwt-auth/$', obtain_jwt_token),
    re_path(r'^api-jwt-auth/refresh/$', refresh_jwt_token),
    re_path(r'^api-jwt-auth/verify/$', verify_jwt_token),

    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
