from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CitaForm
import pyrebase
from dateutil import parser
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from .models import Cita  # Asumiendo que tienes un modelo Cita

# Configuración inicial de Firebase
firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
db = firebase.database()

# Función para crear citas en Firebase
def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['fecha_hora'] = data['fecha_hora'].isoformat() if data['fecha_hora'] else None
            data['precio_total'] = float(data['precio_total'])
            data['iva_incluido'] = form.cleaned_data.get('iva_incluido', False)
            db.child("citas").push(data)
            return redirect('citas:ver_citas')
        else:
            return render(request, 'citas/crear_cita.html', {'form': form})
    else:
        form = CitaForm()
        return render(request, 'citas/crear_cita.html', {'form': form})

# Nueva función para servir los datos de citas a FullCalendar
def citas_json(request):
    citas_raw = db.child("citas").get().val()
    eventos = []
    if citas_raw:
        for key, value in citas_raw.items():
            fecha_hora = parser.parse(value['fecha_hora']) if 'fecha_hora' in value and value['fecha_hora'] else None
            if fecha_hora:
                eventos.append({
                    'title': f"{value.get('cliente', 'Desconocido')}",
                    'start': fecha_hora.isoformat(),
                    'end': (fecha_hora + timedelta(hours=1)).isoformat(),  # Asumiendo duración de 1 hora
                    'url': f"/cita/{key}/"  # Asumiendo que existe una ruta para ver detalles de la cita
                })
    return JsonResponse(eventos, safe=False)
# def citas_json(request):
#     data = [
#         {"title": "Consulta Inicial", "start": "2024-04-20T10:00:00", "end": "2024-04-20T11:00:00", "url": "/cita/1234"},
#         {"title": "Seguimiento", "start": "2024-04-21T12:00:00", "end": "2024-04-21T13:00:00", "url": "/cita/1235"}
#     ]
#     return JsonResponse(data, safe=False)



def ver_citas(request):
    return render(request, 'citas/ver_citas.html')




def cita_detalle(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)  # Asegúrate de que esto coincida con cómo se identifican tus citas
    return render(request, 'citas/cita_detalle.html', {'cita': cita})