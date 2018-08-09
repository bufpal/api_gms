from rest_framework import serializers
from  .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user_pk = serializers.ReadOnlyField(source='user.pk')
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = (
            'pk',
            'user_pk',
            'user_username',
            'fbuid',
            'ospid',
            'school',
            'phone_number',
            'latlng',
            'level',
            'avatar',
        )


class ProfileListSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    user_pk = serializers.ReadOnlyField(source='user.pk')
    post_count = serializers.SerializerMethodField(read_only=True)
    like_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'pk',
            'user_pk',
            'user_username',
            'fbuid',
            'ospid',
            'avatar',
            'phone_number',
            'latlng',
            'post_count',
            'like_count',
            'level',
            'school',
        )
    
    def get_post_count(self, obj):
        if obj.user.post_set.all():
            count = obj.user.post_set.all().count()
        else:
            count = 0
        return count

    def get_like_count(self, obj):
        like_count = 0
        for post in obj.user.post_set.all():
            like_count += post.likes.count()
        return like_count