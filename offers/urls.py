from django.urls import path 
from .views import (
    OffersListView ,OfferDetailView , offer_search,
    ReviewCreateView , ReviewDetailView, ReviewUpdateView,ReviewDeleteView , #ReviewsListView
)

urlpatterns=[
    path('',OffersListView.as_view(),name='offers_list'),
    path('<int:offer_id>/',OfferDetailView.as_view(), name='offer_detail'), 
    path('search/', offer_search, name='offer_search'),
    
    # reviews related urls
    # path('<int:offer_id>/reviews/', ReviewsListView.as_view(), name='reviews_list'),
    path('<int:offer_id>/reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('<int:offer_id>/reviews/<int:review_id>/', ReviewDetailView.as_view(), name='review_detail'),
    path('<int:offer_id>/reviews/<int:review_id>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('<int:offer_id>/reviews/<int:review_id>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]



# from django.conf import settings
# from django.conf.urls.static import static

# if settings.DEBUG:  # Only for development
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
