from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from gallery.forms import PhotoForm
from gallery.models import Photo


class PhotoCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'photo_create.html'
    model = Photo
    form_class = PhotoForm
    success_message = 'Статья создана'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

class PhotoUpdateView(PermissionRequiredMixin,UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    permission_required = 'gallery.photo_change'
    def get_success_url(self):
        return reverse('index')


class PhotoDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'photo_confirm_delete.html'
    model = Photo
    permission_required = 'gallery.photo_delete'
    success_url = reverse_lazy('index')