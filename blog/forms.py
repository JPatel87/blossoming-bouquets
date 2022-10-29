""" Imports from django and post and comment model. """
from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):
    """
    Add post form for admin only.
    """

    class Meta:
        """ Define form fields. """
        model = Post
        fields = ('title', 'slug', 'body', 'image')

    def clean_title(self):
        """ Capitalize post title. """
        return self.cleaned_data['title'].capitalize()

    def clean_body(self):
        """ Capitalize body text."""
        return self.cleaned_data['body'].capitalize()


class CommentForm(forms.ModelForm):
    """
    Comment form for authenticated users.
    """

    class Meta:
        """ Define form fields and labels. """
        model = Comment
        fields = ('name', 'body')
        labels = {
            'name': "Name",
            'body': "Comment",
        }

    def clean_name(self):
        """ Capitalize author names. """
        return self.cleaned_data['name'].capitalize()

    def clean_body(self):
        """ Capitalize body text. """
        return self.cleaned_data['body'].capitalize()
