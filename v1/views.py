from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.generics import ListAPIView, ListCreateAPIView 
from rest_framework.response import Response
from .models import (Inquiry, InquiryComment,
                     Notice, NoticeComment,
                     Post, PostComment,
                     Faq, FaqComment)
from .serializers import (InquirySerializer, InquiryCommentSerializer,
                          NoticeSerializer, NoticeCommentSerializer,
                          PostSerializer, PostCommentSerializer,
                          FaqSerializer, FaqCommentSerializer)


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all().select_related('user')
    serializer_class = InquirySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.query_params.get('user', None)
        if user is not None:
            qs = qs.filter(user__pk = user)
        return qs

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user,
        )


    @ detail_route(methods=['get'])
    def like(self, request, pk):
        inquiry = get_object_or_404(Inquiry, pk=pk)
        user = self.request.user

        updated = False
        liked = False

        if user.is_authenticated():
            if user in inquiry.likes.all():
                liked = False
                inquiry.likes.remove(user)
                inquiry.save()
            else:
                liked = True
                inquiry.likes.add(user)
                inquiry.save()
            updated = True

        data = {
            'updated': updated,
            'liked': liked,
        }

        return Response(data, status=200)


class InquiryCommentViewSet(viewsets.ModelViewSet):
    queryset = InquiryComment.objects.all().select_related('user')
    serializer_class = InquiryCommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('user')
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q =  self.request.query_params.get('q', None)
        if q is not None:
            qs = qs.filter(school__icontains=q)
        return qs

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user,
        )


    @ detail_route(methods=['get'])
    def like(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = self.request.user

        updated = False
        liked = False

        if user.is_authenticated():
            if user in post.likes.all():
                liked = False
                post.likes.remove(user)
                post.save()
            else:
                liked = True
                post.likes.add(user)
                post.save()
            updated = True

        data = {
            'updated': updated,
            'liked': liked,
        }

        return Response(data, status=200)


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all().select_related('user')
    serializer_class = PostCommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user
        )


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        notice_type = self.request.query_params.get('type', None)
        if notice_type is not None:
            qs = qs.filter(notice_type=notice_type)
        return qs


class NoticeCommentViewSet(viewsets.ModelViewSet):
    queryset = NoticeComment.objects.all()
    serializer_class = NoticeCommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user
        )


class FaqViewSet(viewsets.ModelViewSet):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqCommentViewSet(viewsets.ModelViewSet):
    queryset = FaqComment.objects.all().select_related('user')
    serializer_class = FaqCommentSerializer

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user
        )