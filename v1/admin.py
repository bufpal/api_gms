from django.contrib import admin
from .models import (Inquiry, InquiryComment,
                     Notice, NoticeComment,
                     Post, PostComment,
                     Faq, FaqComment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_at']
    list_display_links = ['id', 'user', 'title', 'created_at']

    search_fields = ['title']


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'comment', 'created_at']
    list_display_links = ['id', 'user', 'post', 'comment', 'created_at']

    autocomplete_fields = ['user', 'post']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title', 'created_at']

    search_fields = ['title']

@admin.register(NoticeComment)
class NoticeCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'notice', 'comment', 'created_at']
    list_display_links = ['id', 'user', 'notice', 'comment', 'created_at']

    autocomplete_fields = ['user', 'notice']


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_at']
    list_display_links = ['id', 'user', 'title', 'created_at']

    search_fields = ['title']


@admin.register(InquiryComment)
class InquiryCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'inquiry', 'comment', 'created_at']
    list_display_links = ['id', 'user', 'inquiry', 'comment', 'created_at']

    autocomplete_fields = ['user', 'inquiry']


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at']
    list_display_links = ['pk', 'title', 'content', 'created_at']

    search_fields = ['title']


@admin.register(FaqComment)
class FaqCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'faq', 'comment', 'created_at']
    list_display_links = ['id', 'user', 'faq', 'comment', 'created_at']
    
    autocomplete_fields = ['user', 'faq']