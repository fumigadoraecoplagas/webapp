from django.shortcuts import render, redirect
from .forms import CitaForm
from django.conf import settings
import pyrebase
from dateutil import parser

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
db = firebase.database()

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Convertir datetime a string en formato ISO para JSON
            data['fecha_hora'] = data['fecha_hora'].isoformat() if data['fecha_hora'] else None
            # Convertir Decimal a float
            data['precio_total'] = float(data['precio_total'])
            
            # Revisar si 'iva_incluido' está marcado y asignarlo adecuadamente
            data['iva_incluido'] = form.cleaned_data.get('iva_incluido', False)
            
            # Guardar datos en Firebase
            db.child("citas").push(data)
            return redirect('citas:ver_citas')
        else:
            return render(request, 'citas/crear_cita.html', {'form': form})
    else:
        form = CitaForm()
        return render(request, 'citas/crear_cita.html', {'form': form})

def ver_citas(request):
    citas_raw = db.child("citas").get().val()
    citas = []
    if citas_raw:
        for key, value in citas_raw.items():
            cita = value
            cita['id'] = key
            if 'fecha_hora' in cita and cita['fecha_hora']:
                # Convertir la cadena ISO 8601 a datetime
                cita['fecha_hora'] = parser.parse(cita['fecha_hora'])
            else:
                cita['fecha_hora'] = 'Fecha no disponible'
            citas.append(cita)
        # Ordenar las citas por la fecha y hora
        citas.sort(key=lambda x: x['fecha_hora'] if x['fecha_hora'] != 'Fecha no disponible' else '')
    return render(request, 'citas/ver_citas.html', {'citas': citas})