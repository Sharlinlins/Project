from django.contrib.auth.models import User, Group
from rest_framework import serializers
from myblog.models import Post, Comment, Profile

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image', 'likes', 'post_date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'name', 'body', 'date_added')
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url')