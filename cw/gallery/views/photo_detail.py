from django.views.generic import DetailView
from gallery.models import Photo


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.object
        comments = photo.comments.all()
        context['comments'] = comments
        return context