
from django import forms
from .models import RegistroBiologico, Proyecto, Ecorregion


class EcorregionForm(forms.ModelForm):
    class Meta:
        model = Ecorregion
        fields = [
            'nombre'
            
        ]
        labels = {
            'nombre': 'Ecorregion',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de la ecorregión'
        })
        


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'nombre',
            'descripcion'
        ]
        labels = {
            'nombre': 'Nombre de proyecto',
            'descripcion': 'Descripción'

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control'
        })


class RegistroForm(forms.ModelForm):
   
    class Meta:
        model = RegistroBiologico
        fields = [
            'especie',
            'familia',
            'nombre_comun',
            'proyecto',
            'base_registro',
            'identificador',
            'anio_identificacion',
            'departamento',
            'municipio',
            'localidad',
            'latitud',
            'longitud',
            'autor',
            'fecha_captura',
            'ecorregion'
        ]
        labels = {
            'especie': 'Especie',
            'familia':  'Familia',
            'nombre_comun': 'Nombre común',
            'proyecto': 'Proyecto',
            'base_registro': 'Base registro',
            'identificador': 'Identificador',
            'anio_identificacion': 'Año identificación',
            'departamento': 'Departamento',
            'municipio': 'Municipio',
            'localidad': 'Localidad',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'autor': 'Autor',
            'fecha_captura': 'Fecha captura',
            'ecorregion': 'Ecorregion'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.fields #diccionario que almacena los inputs del formulario
        self.fields['especie'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['familia'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['nombre_comun'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['proyecto'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['base_registro'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['identificador'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': ''
        })
        self.fields['anio_identificacion'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['departamento'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['municipio'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': ''
        })
        self.fields['localidad'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['latitud'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['latitud'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['longitud'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['autor'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['fecha_captura'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Formato aaaa-mm-dd'
        })
        self.fields['ecorregion'].widget.attrs.update({
            'class': 'form-control'
        })
        

