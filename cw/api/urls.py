from django.urls import include, path
from rest_framework import routers
from api.views import FavoriteView, PhotoView

router = routers.DefaultRouter()
router.register('photos', PhotoView)
router.register('favorites', FavoriteView)

urlpatterns = [
    path('', include(router.urls)),
    path('image/<int:pk/fav', FavoriteView.as_view({'get''addfavorite'})),
    path('image/<int:pk/remove', FavoriteView.as_view({'get''removefavorite'})),
]
