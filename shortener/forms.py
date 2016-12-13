from django import forms

from django.core.validators import URLValidator

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL')

    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        url = cleaned_data['url']
        print(url)

    def clean_url(self):
        url = self.cleaned_data['url']
        return url
