from django.urls import path
from .views import blogView, blog_post_view, new_post_view, update_post

urlpatterns = [
    path('', blogView.as_view(), name="renureads"),
    path('blog/<int:pk>/', blog_post_view.as_view(), name="blog-view"),
    path('blog/new_post/', new_post_view.as_view(), name="new_post"),
    path('blog/update/<int:pk>/', update_post.as_view(), name="update_post"),
]
