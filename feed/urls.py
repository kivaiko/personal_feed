from django.urls import path
from .views import FeedEventListView

urlpatterns = [
    path("", FeedEventListView.as_view(), name="feed-list"),
]
