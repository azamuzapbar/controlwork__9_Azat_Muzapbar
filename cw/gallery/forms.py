from django import forms
from gallery.models import Photo, Comment



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'image']
        widgets = {'description': forms.TextInput(attrs={'class': 'form-control'}),
                   'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        post_pk = kwargs.pop('post_pk', None)
        super().__init__(*args, **kwargs)
        self.post_pk = post_pk

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.post_id = self.post_pk
        if commit:
            comment.save()
        return comment