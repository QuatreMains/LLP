from django import forms
from .models import Blog


class BlogPost(forms.ModelForm):  # 모델을 기반으로 한 입력공간
    class Meta:
        model = Blog
        fields = ['title', 'body']
