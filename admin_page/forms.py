from django import forms
from v1.models import InquiryComment, Notice

class InquiryCommentForm(forms.ModelForm):

    class Meta:
        model = InquiryComment
        fields = ['comment']


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'notice_type', 'content', 'survey_link', 'photo']