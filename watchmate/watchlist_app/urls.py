from django.urls import path, include
#from .views import movie_list, movie_details

from .views import WatchListAV, WatchDetailAV, StreamPlatform, StreamPlatformDetails,ReviewDetail,ReviewList, ReviewCreate
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('list/<int:pk>', WatchDetailAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatform.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetails.as_view(), name='stream-details'),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]

