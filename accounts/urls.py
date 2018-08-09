from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, ProfileListView

app_name = 'accounts'

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path(r'^profile-list/$', ProfileListView.as_view(), name='profile-list')
]