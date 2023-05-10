from django import forms

class urlform(forms.Form):
    url_search = forms.CharField(max_length = 500)