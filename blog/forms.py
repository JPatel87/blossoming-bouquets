"""Imports from django and post and comment model."""
from django import forms
from .models import Post, Comment

class AddPostForm(forms.ModelForm):
    """Add post form used to add posts for admin only."""

    class Meta:
        """Class to define form fields."""
        model = Post
        fields = ('title', 'slug', 'body', 'image')

    def clean_title(self):
        """Method to capitalize post title from add post form."""
        return self.cleaned_data['title'].capitalize()

    def clean_body(self):
        """Method to capitalize body text from add post form."""
        return self.cleaned_data['body'].capitalize()


class CommentForm(forms.ModelForm):
    """Add comment form used to add comments for authenticated users."""

    class Meta:
        """Class to define form fields and labels."""
        model = Comment
        fields = ('name', 'body')
        labels = {
            'name': "Name",
            'body': "Comment",
        }

    def clean_name(self):
        """Method to capitalize names from comments form."""
        return self.cleaned_data['name'].capitalize()

    def clean_body(self):
        """Method to capitalize body text from comments form."""
        return self.cleaned_data['body'].capitalize()
