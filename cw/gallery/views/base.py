from django.views.generic import ListView
from gallery.models import Photo


class IndexView(ListView):
    context_object_name = 'photos'
    model = Photo
    template_name = 'index.html'
    ordering = ['-created_at']