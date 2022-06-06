from django import forms

from tabela.models import Dataset, Source


class datasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['tipofonte']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipofonte'].queryset = Source.objects.all()
