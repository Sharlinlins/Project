from django.urls import path, include
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns = [
	path('', include(router.urls)),
]