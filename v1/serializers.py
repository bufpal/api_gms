from rest_framework import serializers
from .models import (Inquiry, InquiryComment,
                     Notice, NoticeComment,
                     Post, PostComment,
                     Faq, FaqComment)
from accounts.models import Profile


class InquiryCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    user_lv = serializers.SerializerMethodField()
    user_pk = serializers.SerializerMethodField()

    class Meta:
        model = InquiryComment
        fields = (
            'pk',
            'user',
            'user_lv',
            'user_pk',
            'avatar',
            'inquiry',
            'comment',
            'created_at'
        )
    
    def get_user(self, obj):
        return str(obj.user.username)

    def get_user_lv(self, obj):
        try:
            user = Profile.objects.get(user_id=obj.user.pk)
        except Profile.DoesNotExist:
            return ''    
        
        return str(user.level)

    def get_user_pk(self, obj):
        return str(obj.user.pk)


class InquirySerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    user_pk = serializers.ReadOnlyField(source='user.pk')
    user_lv = serializers.SerializerMethodField()
    comment_set = InquiryCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Inquiry
        fields = (
            'pk', 'user_pk', 'user_username', 'user_lv', 'avatar',
            'title', 'message', 'school', 'comment_set', 'likes',
            'created_at',)

    def get_user_lv(self, obj):
        try:
            user = Profile.objects.get(user_id=obj.user.pk)
        except Profile.DoesNotExist:
            return ''    
        
        return str(user.level)


class PostCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    user_lv = serializers.SerializerMethodField()

    class Meta:
        model = PostComment
        fields = ('pk', 'user', 'user_lv', 'post', 'comment', 'avatar', 'created_at',)
    
    def get_user(self, obj):
        return str(obj.user.username)

    def get_user_lv(self, obj):
        try:
            user = Profile.objects.get(user_id=obj.user.pk)
        except Profile.DoesNotExist:
            return ''    
        
        return str(user.level)


class PostSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    user_pk = serializers.ReadOnlyField(source='user.pk')
    user_lv = serializers.SerializerMethodField()
    comment_set = PostCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'user_pk', 'user_username', 'user_lv', 'title', 'message', 'avatar', 'comment_set', 'likes', 'school', 'created_at',)

    def get_user_lv(self, obj):
        user = Profile.objects.get(user_id=obj.user.pk)
        return str(user.level)


class NoticeCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    user_lv = serializers.SerializerMethodField()

    class Meta:
        model = NoticeComment
        fields = ('pk', 'user', 'user_lv', 'notice', 'comment', 'avatar', 'created_at',)

    
    def get_user(self, obj):
        return str(obj.user.username)

    
    def get_user_lv(self, obj):
        try:
            user = Profile.objects.get(user_id=obj.user.pk)
        except Profile.DoesNotExist:
            return ''    
        
        return str(user.level)


class NoticeSerializer(serializers.ModelSerializer):
    comment_set = NoticeCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Notice
        fields = ('pk', 'title', 'notice_type', 'photo', 'content','survey_link', 'comment_set', 'created_at',)


class FaqCommentSerializer(serializers.ModelSerializer):
    user_pk = serializers.ReadOnlyField(source='user.pk')
    user_username = serializers.ReadOnlyField(source='user.username')

    user_lv = serializers.SerializerMethodField()

    class Meta:
        model = FaqComment
        fields = ('pk', 'user_pk', 'user_username', 'user_lv', 'faq', 'comment', 'avatar', 'created_at')

    def get_user_lv(self, obj):
        try:
            user = Profile.objects.get(user_id=obj.user.pk)
        except Profile.DoesNotExist:
            return ''    
        
        return str(user.level)


class FaqSerializer(serializers.ModelSerializer):
    comment_set = FaqCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Faq
        fields = ('pk', 'title', 'faq_type', 'content', 'comment_set', 'created_at')