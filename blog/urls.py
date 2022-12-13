from django.urls import path
from .views import blogView, blog_post_view, new_post_view, update_post, delete_post, add_comment, delete_comment

urlpatterns = [
    path('', blogView.as_view(), name="renureads"),
    path('blog/<int:pk>/', blog_post_view.as_view(), name="blog-view"),
    path('blog/new_post/', new_post_view.as_view(), name="new_post"),
    path('blog/update/<int:pk>/', update_post.as_view(), name="update_post"),
    path('blog/delete/<int:pk>/', delete_post.as_view(), name="delete_post"),
    path('blog/<int:pk>/comment/', add_comment.as_view(), name="add_comment"),
    path('blog/<int:pk>/delete/', delete_comment.as_view(), name="delete_comment"),


]
