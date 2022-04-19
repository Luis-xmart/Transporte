from django import forms
from Vehiculos.models import Vehiculo

# class FormularioConductores(forms.Form):
#     vehiculo = forms.ModelChoiceField(queryset=Vehiculo.objects.all(), label="Vehiculo", required=True)

class FormularioConductores(forms.ModelForm):
    vehiculos = forms.ChoiceField(choices=[(doc.id, doc.placa) for doc in Vehiculo.objects.all()])
    class Meta:
        model = Vehiculo
        fields = ['vehiculos', ]
        widgets = {
            'vehiculos': forms.Select(attrs={'class': 'select'}),
        }