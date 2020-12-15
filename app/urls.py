from django.urls import path
from app.views import (
  index,
  PostListView,
  post_detail,
  PostCreateView,
  post_edit,
  PostEditView,
  post_delete,
  PostDetail,
  PostDeleteView,
  UserProfileView,
  comment_create,
  CommentCreateView,
  CommentEditView,
  CommentDeleteView,
)

urlpatterns = [
  path('', index, name='post_list'),
  path('', PostListView.as_view(), name='post_list'),
  path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
  path('post/create', PostCreateView.as_view(), name='post_create'),
  path('post/<int:pk>/edit', post_edit, name='post_edit'),
  path('post/<int:pk>/edit', PostEditView.as_view(), name='post_edit'),
  path('post/<int:pk>/delete', post_delete, name='post_delete'),
  path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
  path('post/<int:pk>/comment/create', comment_create, name='comment_create'),
  path('post/<int:pk>/comment/create', CommentCreateView.as_view(), name='comment_create'),
  path('post/<int:pk>/comment/<int:pk_comment>/edit', CommentEditView.as_view(), name='comment_edit'),
  path('post/<int:pk>/comment/<int:pk_comment>/delete', CommentDeleteView.as_view(), name='comment_delete'),
  path('userprofile', UserProfileView.as_view(), name='user_profile'),
]
