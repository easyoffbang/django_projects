from django.views.generic import CreateView
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    #success_url = '/...'


post_new = PostCreateView.as_view()
