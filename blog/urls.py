from django.urls import path
from .views import blogView

urlpatterns = [
    path('blog/', blogView.as_view(), name="renureads"),
]
