from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from gallery.forms import CommentForm
from gallery.models import Comment,Photo




class CommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'comment_create.html'
    form_class = CommentForm

    def form_valid(self, form):
        photo_pk = self.kwargs['pk']
        text = form.cleaned_data['text']
        photo = get_object_or_404(Photo, pk=photo_pk)
        form.instance.author = self.request.user
        form.instance.photo = photo
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        post_pk = self.kwargs['pk']
        return reverse_lazy('photo_detail', kwargs={'pk': post_pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['post_pk'] = self.kwargs['pk']
        return kwargs