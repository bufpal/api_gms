from django.conf import settings
from django.db import models
from django.urls import reverse


class Inquiry(models.Model):
    SCHOOL = (
        ('a', '삼육대학교'),
        ('b', '한국국제대학교'),
        ('c', '한국전기직업전문학교'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    avatar = models.CharField(max_length=600, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='inquirylike_set')
    school = models.CharField(max_length=1, choices=SCHOOL)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('admin-page:inquiry-detail', args=[self.id])


class InquiryComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    inquiry = models.ForeignKey(Inquiry, related_name='comment_set', on_delete=models.CASCADE)
    comment = models.TextField()
    avatar = models.CharField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    SCHOOL = (
        ('a', '삼육대학교'),
        ('b', '한국국제대학교'),
        ('c', '한국전기직업전문학교'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    avatar = models.CharField(max_length=600, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='postlike_set')
    school = models.CharField(max_length=1, choices=SCHOOL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.message
        

class PostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment_set', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    avatar = models.CharField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


class Notice(models.Model):
    TYPE = (
        ('a', 'Notice'),
        ('b', 'Survey'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    notice_type = models.CharField(max_length=1, choices=TYPE)
    survey_link = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='notice/%Y/%M/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('admin-page:notice-detail', args=[self.id])

class NoticeComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, related_name='comment_set', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    avatar = models.CharField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.comment


class Faq(models.Model):
    title = models.CharField(max_length=200)
    faq_type = models.CharField(max_length=1, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.title


class FaqComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    faq = models.ForeignKey(Faq, related_name='comment_set', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    avatar = models.CharField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.comment
