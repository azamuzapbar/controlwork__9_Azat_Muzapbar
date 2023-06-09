from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from api.serializers import PhotoSerializer, CommentSerializer, FavoriteSerializer
from gallery.models import Photo, Comment, Favorite


class PhotoView(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request):
        return self.create()

    def delete(self, request, pk):
        self.destroy()


class FavoriteView:
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def addfavorite(self, request, *args, **kwargs):
        photo_by_pk = self.get_object()
        user_from_request = request.user
        user_from_request.favorited_photos.add(photo_by_pk)
        return JsonResponse({'key': 'Добавлено'})

    def deletefavorite(self, request, *args, **kwargs):
        photo_by_pk = self.get_object()
        user_from_request = request.user
        user_from_request.favorited_photos.remove(photo_by_pk)
        return JsonResponse({'key': 'Удалено'})
