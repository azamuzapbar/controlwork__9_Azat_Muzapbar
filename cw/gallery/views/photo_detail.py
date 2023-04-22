from django.views.generic import DetailView

from gallery.models import Photo


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo.html'

