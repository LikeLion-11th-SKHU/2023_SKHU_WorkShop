from django import forms
from .models import WorkShop

class Workshop_Form(forms.ModelForm):
    class Meta:
        model = WorkShop
        fields = ['comment']
        labels = {
        'comment' : '댓글' , #html, 댓글: 바꾸려면 이거 fix
         'like' : '좋아요',
        'dislike': '싫어요',
        'sad' : '슬퍼요',
        }


