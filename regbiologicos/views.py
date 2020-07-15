from django.shortcuts import render, redirect, reverse

#formularios
from .forms import RegistroForm, ProyectoForm, EcorregionForm

#django utilities
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

#mis modelos
from .models import RegistroBiologico,Proyecto,Ecorregion


#django views
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView

import csv


#proyectos

def proyectos_list(request):
    if request.method=='GET':
        form = ProyectoForm()
        proyectos = Proyecto.objects.all()

        return render(request,'regbiologicos/proyectos.html', {'form': form, 'proyectos': proyectos })

    else:
        form = ProyectoForm(request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form_valid = form.save(commit=False)
            form_valid.save()

            #messages.success(request, 'Proyecto creado exitosamente')
            
            return HttpResponse("Ok")

        # return render(request, 'regbiologicos/proyectos.html', {
        #     'form': form
        #})


class ProyectoUpdateView(SuccessMessageMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'regbiologicos/updateproyecto.html'
    success_message = 'Registro actualizado exitosamente'
    
    def get_success_url(self):
        return reverse('regbiologicosapp:proyectos')

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'regbiologicos/deleteproyecto.html'
    success_url = reverse_lazy('regbiologicosapp:proyectos')


#ecorregion
def ecorregion_list(request):
    if request.method=='GET':
        form = EcorregionForm()
        ecorregiones = Ecorregion.objects.all()

        return render(request,'regbiologicos/ecorregiones.html', {'form': form, 'ecorregiones': ecorregiones })

    else:
        form = EcorregionForm(request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form_valid = form.save(commit=False)
            form_valid.save()

            messages.success(request, 'Ecorregión creado exitosamente')
            return redirect('regbiologicosapp:ecorregiones')

        return render(request, 'regbiologicos/ecorregiones.html', {
            'form': form
        })

class EcorregionUpdateView(SuccessMessageMixin, UpdateView):
    model = Ecorregion
    form_class = EcorregionForm
    template_name = 'regbiologicos/updateecorregion.html'
    success_message = 'Registro actualizado exitosamente'
    
    def get_success_url(self):
        return reverse('regbiologicosapp:ecorregiones')

class EcorregionDeleteView(DeleteView):
    model = Ecorregion
    template_name = 'regbiologicos/deleteecorregion.html'
    success_url = reverse_lazy('regbiologicosapp:ecorregiones')



#registro de especies
def registros_biologicos(request):

    if request.method=='GET':
        form = RegistroForm()
        reg_bio = RegistroBiologico.objects.all()

        return render(request,'regbiologicos/regbiologicos.html', {'form': form, 'regbio': reg_bio })

    else:
        form = RegistroForm(request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form_valid = form.save(commit=False)
            form_valid.save()

            messages.success(request, 'Registro biológico creado exitosamente')
            return redirect('regbiologicosapp:registros_biologicos')

        return render(request, 'regbiologicos/regbiologicos.html', {
            'form': form
        })

class RegistroBiologicoUpdateView(SuccessMessageMixin, UpdateView):
    model = RegistroBiologico
    form_class = RegistroForm
    template_name = 'regbiologicos/updateregbiologico.html'
    success_message = 'Registro actualizado exitosamente'
    
    def get_success_url(self):
        return reverse('regbiologicosapp:registros_biologicos')

class RegistroBiologicoDeleteView(DeleteView):
    model = RegistroBiologico
    template_name = 'regbiologicos/deleteregistrosbiologico.html'
    success_url = reverse_lazy('regbiologicosapp:registros_biologicos')


#exporta a csv
def export_registros_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registroespecies.csv"'

    writer = csv.writer(response)
    writer.writerow(['Especie', 'Familia', 'Nombre comun','Proyecto' ,'Base registro', 'Identificador', 'Departamento', 'Municipio','Localidad','Latitud','Longitud','Autor','Fecha captura','Ecorregion' ])
    especies = RegistroBiologico.objects.values('especie','familia','nombre_comun','proyecto__nombre','base_registro','identificador','anio_identificacion','departamento','municipio','localidad','latitud','longitud','autor','fecha_captura','ecorregion__nombre').values_list('especie','familia','nombre_comun','proyecto__nombre','base_registro','identificador','anio_identificacion','departamento','municipio','localidad','latitud','longitud','autor','fecha_captura','ecorregion__nombre')
    
    for especie in especies:
	    writer.writerow(especie)

    return response  

def export_proyectos_csv_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="proyectos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre del proyecto', 'Descripción' ])
    proyectos = Proyecto.objects.values_list('nombre','descripcion')
    
    for p in proyectos:
	    writer.writerow(p)

    return response  

def export_ecorregion_csv_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ecorregiones.csv"'

    writer = csv.writer(response)
    writer.writerow(['Ecorregión'])
    ecorregiones = Ecorregion.objects.values_list('nombre')
    
    for p in ecorregiones:
	    writer.writerow(p)

    return response  








        
