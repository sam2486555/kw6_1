from django.forms import ModelForm, BooleanField

from blog.models import Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content", "publish_at",)
