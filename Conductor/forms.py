
from django import forms
from .models import Entrega, Observaciones


class FormularioEntrega(forms.Form):
    observacion = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

class FormularioEntrega2(forms.ModelForm):
    class Meta:
        model = Observaciones
        fields = ('observacion',)
        labels = {'observacion': 'Observaciones'}
        widgets = {'observacion': forms.Textarea(attrs={'rows': 5, 'cols': 40})}


