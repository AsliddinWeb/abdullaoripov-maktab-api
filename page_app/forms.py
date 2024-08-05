from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Page

class PageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Page
        fields = '__all__'
