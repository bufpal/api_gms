from django.conf import settings
from django.db import models

class Profile(models.Model):
    SCHOOL_LIST = (
        ('a', '삼육대학교'),
        ('b', '한국전기직업전문학교'),
        ('c', '한국국제대학교')
    )

    LEVEL_STATUS = (
        ('Lv1', 'Lv1'),
        ('Lv2', 'Lv2'),
        ('Lv3', 'Lv3'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fbuid = models.CharField(max_length=300)
    ospid = models.CharField(max_length=300)
    school = models.CharField(max_length=1, choices=SCHOOL_LIST, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=3, choices=LEVEL_STATUS, blank=True)
    avatar = models.CharField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.username