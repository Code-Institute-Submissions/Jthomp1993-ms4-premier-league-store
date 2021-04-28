from django import forms
from products.widgets import CustomClearableFileInput
from .models import Comments, News


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment', ]


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
