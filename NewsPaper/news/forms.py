from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'postCategory',
            'title',
            'text',
            'rating',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("title")
        if description is not None and len(description) > 70:
            raise ValidationError({
                "title": "Название не может быть более 70 символов."
            })

        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data