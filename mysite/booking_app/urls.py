from django.urls import path
from .views import *


urlpatterns = [
    path('profile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('profile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='product_detail'),

    path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='product_detail'),
    path('hotelImage/', HotelImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('hotelImage/<int:pk>/', HotelImageViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='product_detail'),

    path('room/', RoomDetailViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('room/<int:pk>/', RoomDetailViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='product_detail'),
    path('roomImage/', RoomImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('roomImage/<int:pk>/', RoomImageViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='product_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='product_detail'),

    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='product_detail'),



]