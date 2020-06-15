from django import forms
from .models import Post


# Form extends Model Form
class PostForm(forms.ModelForm):

    # Define the model type to save the form as, and the fields that the form should accept
    class Meta:
        model = Post
        fields = ('title', 'text')