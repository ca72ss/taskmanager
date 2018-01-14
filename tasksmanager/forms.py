from django import forms
from.models import Photo,Task,Video,User
from django.forms.models import inlineformset_factory


class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=10000, widget=forms.Textarea)
    is_complete = forms.BooleanField
    user = forms.ModelMultipleChoiceField(queryset=User.objects.filter(groups__name='Students'))

    class Meta:
        model = Task
        fields = ['name', 'description', 'is_complete', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'required': True, }),
        }


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ImageField)

    class Meta:
        model = Photo
        fields = ['image']


class VideoForm(forms.ModelForm):
    video = forms.CharField(max_length=50)

    class Meta:
        model = Video
        fields = ['video']
