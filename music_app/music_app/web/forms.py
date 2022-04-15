from django import forms

from music_app.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['placeholder'] = name.capitalize()

    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            albums = Album.objects.all()
            self.instance.delete()
            albums.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'name':
                field.widget.attrs['placeholder'] = 'Album Name'
            elif name == 'image_url':
                field.widget.attrs['placeholder'] = 'Image URL'
            else:
                field.widget.attrs['placeholder'] = name.capitalize()

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL',
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL',
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            # field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL',
        }
