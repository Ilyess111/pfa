from django.urls import path
from .views import (
    ReviewDetailView, ReviewCreateView,
    ReviewUpdateView, ReviewDeleteView
)

urlpatterns = [
    path("<int:pk>/detail/", ReviewDetailView.as_view(), name="review_detail"),
    path("new/", ReviewCreateView.as_view(), name="review_create"),
    path("<int:pk>/edit/", ReviewUpdateView.as_view(), name="review_update"),
    path("<int:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"),
]
