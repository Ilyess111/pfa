from django.urls import path 
from .views import OffersListView ,OfferDetailView , offer_search

urlpatterns=[
    path('',OffersListView.as_view(),name='offers_list'),
    path('<int:pk>/',OfferDetailView.as_view(), name='offer_detail'), 
    path('search/', offer_search, name='offer_search'),
]



from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:  # Only for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
