from django import forms
from gallery.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'image']
        widgets = {'description': forms.TextInput(attrs={'class': 'form-control'}),
                   'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})}
