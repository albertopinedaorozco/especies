from django.urls import path

from .views import *


app_name = 'regbiologicosapp'

urlpatterns = [
    path('', registros_biologicos, name='registros_biologicos'),
    path('editar/<int:pk>', RegistroBiologicoUpdateView.as_view(), name = 'update'),
    path('eliminar/<int:pk>', RegistroBiologicoDeleteView.as_view(), name = 'delete'),
    path('export/csv', export_registros_csv, name='export_registros_csv_list'),

    path('proyecto', proyectos_list, name='proyectos'),
    path('proyecto/editar/<int:pk>', ProyectoUpdateView.as_view(), name = 'update_proyecto'),
    path('proyecto/eliminar/<int:pk>', ProyectoDeleteView.as_view(), name = 'delete_proyecto'),
    path('export/proyectos/csv', export_proyectos_csv_list, name='export_proyectos_csv_list'),

    path('ecorregion', ecorregion_list, name='ecorregiones'),
    path('ecorregion/editar/<int:pk>', EcorregionUpdateView.as_view(), name = 'update_ecorregion'),
    path('ecorregion/eliminar/<int:pk>', EcorregionDeleteView.as_view(), name = 'delete_ecorregion'),
    path('export/ecorregion/csv', export_ecorregion_csv_list, name='export_ecorregion_csv_list'),
   
]