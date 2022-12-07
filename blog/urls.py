from django.urls import path
from .views import blogView, blog_post_view

urlpatterns = [
    path('', blogView.as_view(), name="renureads"),
    path('blog/<int:pk>/', blog_post_view.as_view(), name="blog-view")
]
