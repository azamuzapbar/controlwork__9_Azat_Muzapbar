from django.urls import include, path
from rest_framework import routers
from api.views import FavoriteView, PhotoView, CommentView

router = routers.DefaultRouter()
router.register('photos', PhotoView)
router.register('favorites', FavoriteView)
router.register('comments', CommentView)
urlpatterns = [
    path('', include(router.urls)),

    # path('photo/<int:pk/fav', FavoriteView.as_view({'get''addfavorite'})),
    # path('photo/<int:pk/remove', FavoriteView.as_view({'get''removefavorite'})),
]
