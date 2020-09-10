from django.urls import path
from . import views as v
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', v.index, name="index"),
    path('home/', HomeView.as_view(), name="home"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="details"),
    path('addpost/', AddPostView.as_view(), name="addpost"),
    path('addcategory/', AddCategoryView.as_view(), name="addcategory"),
    path('posts/editpost/<int:pk>', EditPostView.as_view(), name="editpost"),
    path('posts/<int:pk>/remove', DeletePostView.as_view(), name="deletepost"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('posts/<int:pk>/comment/', AddCommentView.as_view(), name="addcomment"),
]
