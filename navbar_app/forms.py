from django import forms
from .models import OneNavbar, TwoNavbar, ThreeNavbar

class TwoNavbarForm(forms.ModelForm):
    class Meta:
        model = TwoNavbar
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set queryset for `one_navbar` based on `is_submenu`
        self.fields['one_navbar'].queryset = OneNavbar.objects.filter(is_submenu=True)

class ThreeNavbarForm(forms.ModelForm):
    class Meta:
        model = ThreeNavbar
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set queryset for `two_navbar` based on `is_submenu`
        self.fields['two_navbar'].queryset = TwoNavbar.objects.filter(is_submenu=True)
