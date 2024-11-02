from django.urls import path
from .views import *

urlpatterns = [


    path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='hotel_detail'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='user_detail'),

    path('room/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                'delete': 'destroy'}), name='room_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='review_detail'),

    path('HotelImage/', HotelImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='HotelImage_list'),
    path('HotelImage/<int:pk>/', HotelImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                           'delete': 'destroy'}), name='HotelImage_detail'),

    path('RoomImage/', RoomImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='RoomImage_list'),
    path('RoomImage/<int:pk>/', RoomImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'}), name='RoomImage_detail'),

    path('Booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='Booking_list'),
    path('Booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='Booking_detail'),

]
