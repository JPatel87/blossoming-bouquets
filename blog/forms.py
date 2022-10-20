from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Post title'}),
    )

    slug = forms.SlugField(
        widget=forms.TextInput(attrs={'placeholder':'Post slug'}),
    )

    body = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Please enter your post details'}),
    )

    image = forms.ImageField(
        label='Image', required=False)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'body',)
