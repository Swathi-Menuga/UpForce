from django.urls import path
from .views import (
    CreateUserView,
    GetUserView,
    UpdateUserView,
    DeleteUserView,
    CreatePostView,
    GetPostView,
    UpdatePostView,
    DeletePostView,
    CreateLikeView,
    GetLikeView,
    UpdateLikeView,
    DeleteLikeView,
    PostListWithLikeCountView,
)

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create-user'),
    path('users/<int:pk>/', GetUserView.as_view(), name='get-user'),
    path('users/<int:pk>/update/', UpdateUserView.as_view(), name='update-user'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='delete-user'),
    path('posts/', CreatePostView.as_view(), name='create-post'),
    path('posts/<int:pk>/', GetPostView.as_view(), name='get-post'),
    path('posts/<int:pk>/update/', UpdatePostView.as_view(), name='update-post'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('likes/', CreateLikeView.as_view(), name='create-like'),
    path('likes/<int:pk>/', GetLikeView.as_view(), name='get-like'),
    path('likes/<int:pk>/update/', UpdateLikeView.as_view(), name='update-like'),
    path('likes/<int:pk>/delete/', DeleteLikeView.as_view(), name='delete-like'),
    path('posts-with-like-count/', PostListWithLikeCountView.as_view(), name='post-list-with-like-count'),
]