from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('gmsweb.urls', namespace='gmsweb')),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('api/v1/', include('v1.urls', namespace='v1')),
    path('admin-page/', include('admin_page.urls', namespace='admin-page')),
    
    path('api-jwt-auth/', obtain_jwt_token),
    path('api-jwt-auth/refresh/', refresh_jwt_token),
    path('api-jwt-auth/verify/', verify_jwt_token),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
