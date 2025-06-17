from django import forms
from blog.models import Post, PostComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',
                  'description',
                  'category')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title ...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description ...'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'reading_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'reading time ...'
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            })
        }

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'w-full p-3 border border-gray-700 rounded-lg bg-slate-900 text-slate-200 focus:border-purple-500 focus:ring-purple-500', 'rows': 5, 'placeholder': 'Ваш комментарий...'}),
        }

