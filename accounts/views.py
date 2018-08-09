from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from .models import Profile
from .serializers import ProfileSerializer, ProfileListSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        if Profile.objects.filter(user=self.request.user):
            ospid = self.request.data.get('ospid','')
            current_user = Profile.objects.get(user=self.request.user)
            
            if current_user.ospid != ospid:
                current_user.ospid=ospid
                current_user.save()

            avatar = self.request.data.get('avatar','')

            if current_user.avatar != avatar:
                current_user.avatar = avatar
                current_user.save()

            latlng = self.request.data.get('latlng', '')

            if current_user.latlng != latlng:
                current_user.latlng = latlng
                current_user.save()
        
            return Response('', status=200)

        else:
            serializer.save(
                user = self.request.user
            )


class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q', None)
        if q is not None:
            qs = qs.filter(fbuid=q)
        
        return qs
