from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'v1'

router = DefaultRouter()

router.register(r'inquiry', views.InquiryViewSet)
router.register(r'inquiry-comment',views.InquiryCommentViewSet)

router.register(r'post', views.PostViewSet)
router.register(r'post-comment', views.PostCommentViewSet)

router.register(r'notice', views.NoticeViewSet)
router.register(r'notice-comment', views.NoticeCommentViewSet)

router.register(r'faq', views.FaqViewSet)
router.register(r'faq-comment', views.FaqCommentViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
]