from django import forms
from .models import Post, Comment


class AddPostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('title', 'slug', 'body', 'image')

    def clean_title(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['title'].capitalize()

    def clean_body(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['body'].capitalize()


class CommentForm(forms.ModelForm):


    class Meta:

        model = Comment
        fields = ('name', 'body')
        labels = {
            'name': "Name",
            'body': '',
        }

    def clean_name(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['name'].capitalize()

    def clean_body(self):
        """
        Method to capitalize first names from bookings form.
        """
        return self.cleaned_data['body'].capitalize()
