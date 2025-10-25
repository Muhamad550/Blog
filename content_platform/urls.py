from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from blog.views import (
    BlogPostListCreateView, BlogPostDetailView,
    CategoryListView, PostsByCategoryView,
    CommentListCreateView, CommentDetailView,
    RegisterView, LoginView, LogoutView
)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/posts/')),
    path('admin/', admin.site.urls),
    path('api/posts/', BlogPostListCreateView.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/categories/<int:category_id>/posts/', PostsByCategoryView.as_view(), name='posts-by-category'),
    path('api/posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls')),
]