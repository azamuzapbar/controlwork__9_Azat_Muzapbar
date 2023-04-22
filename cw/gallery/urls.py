from django.urls import path
from gallery.views.base import IndexView
from gallery.views.photo_add import PhotoCreateView,PhotoUpdateView, PhotoDeleteView
from gallery.views.photo_detail import PhotoDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photos/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photos/<int:pk>/confirm-delete/', PhotoDeleteView.as_view(), name='confirm_delete'),
]
