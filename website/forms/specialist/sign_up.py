from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    city = forms.CharField(required=True)
    comment = forms.CharField(required=False, widget=forms.Textarea)

