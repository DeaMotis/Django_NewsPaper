from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import CreateView

from .models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            #'categoryType',
            'postCategory',
        ]

        labels = {
            'title': 'Title',
            'text': 'Text',
            #'categoryType': 'Type',
            'postCategory': 'Category',
        }

    #def __init__(self, *args, **kwargs):
        #super(PostForm, self).__init__(*args, **kwargs)
        #self.fields['categoryType'].empty_label = 'Выберите категорию'

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("description")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Заголовок не должен совпадать с текстом."
            )

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name

