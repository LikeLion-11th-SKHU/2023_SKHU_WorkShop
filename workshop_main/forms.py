from django import forms
from .models import WorkShop

class Workshop_Form(forms.ModelForm):
    class Meta:
        model = WorkShop
        fields = ['comment', 'emoji']
        labels = {
        'comment' : '댓글' , #html, 댓글: 바꾸려면 이거 fix
        'likes' : '좋아요',
        }

        widgets = {
            'emoji': forms.RadioSelect(),
        }


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]