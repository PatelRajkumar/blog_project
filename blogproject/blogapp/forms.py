# -*- coding: utf-8 -*-
from django import forms
class email_send(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
from .models import Comment
class Comment_form(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','comment')
