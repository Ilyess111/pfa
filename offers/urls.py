from django.urls import path , include
from .views import (
    OffersListView ,OfferDetailView , offer_search,
    ReviewCreateView , ReviewDetailView, ReviewUpdateView,ReviewDeleteView , 
)

urlpatterns=[
    path('',OffersListView.as_view(),name='offers_list'),
    path('<int:offer_id>/',OfferDetailView.as_view(), name='offer_detail'), 
    path('search/', offer_search, name='offer_search'),
    
    
    path('<int:offer_id>/reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('<int:offer_id>/reviews/<int:review_id>/', ReviewDetailView.as_view(), name='review_detail'),
    path('<int:offer_id>/reviews/<int:review_id>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('<int:offer_id>/reviews/<int:review_id>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('',include('bookings.urls'))
]



