from django import forms

from mainapp.models import Goods


class GoodForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
