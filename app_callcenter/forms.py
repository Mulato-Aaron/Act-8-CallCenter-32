from django import forms
from .models import (
    AgenteCallCenter, 
    ClienteCallCenter, 
    Llamada, 
    ProblemaReportado, 
    EncuestaSatisfaccion, 
    Campana,
    ParticipacionCampana
)


class AgenteForm(forms.ModelForm):
    class Meta:
        model = AgenteCallCenter
        fields = [
            "nombre",
            "apellido",
            "email",
            "telefono",
            "fecha_contratacion",
            "salario",
            "turno",
            "habilidades_idiomas",
            "estado_agente",
            "dni",
            "foto",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_contratacion": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "salario": forms.NumberInput(attrs={"class": "form-control"}),
            "turno": forms.TextInput(attrs={"class": "form-control"}),
            "habilidades_idiomas": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "estado_agente": forms.TextInput(attrs={"class": "form-control"}),
            "dni": forms.TextInput(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteCallCenter
        fields = [
            'nombre_empresa',
            'contacto_principal',
            'email_contacto',
            'telefono_contacto',
            'sector',
            'fecha_registro',
            'historial_problemas',
            'nivel_satisfaccion',
            'foto',
        ]
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'email_contacto': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'historial_problemas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'nivel_satisfaccion': forms.NumberInput(attrs={'class': 'form-control'}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
        }
class LlamadaForm(forms.ModelForm):
    class Meta:
        model = Llamada
        fields = [
            'id_cliente',
            'id_agente',
            'fecha_hora_inicio',
            'fecha_hora_fin',
            'duracion_segundos',
            'tipo_llamada',
            'resultado_llamada',
            'grabacion_url',
            'motivo_llamada',
            'calificacion_cliente',
        ]
        widgets = {
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'id_agente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_hora_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'fecha_hora_fin': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'duracion_segundos': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_llamada': forms.TextInput(attrs={'class': 'form-control'}),
            'resultado_llamada': forms.TextInput(attrs={'class': 'form-control'}),
            'grabacion_url': forms.URLInput(attrs={'class': 'form-control'}),
            'motivo_llamada': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'calificacion_cliente': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProblemaReportadoForm(forms.ModelForm):
    class Meta:
        model = ProblemaReportado
        fields = [
            'id_llamada',
            'id_agente_resolvio',
            'descripcion_problema',
            'estado_problema',
            'fecha_resolucion_estimada',
            'prioridad',
            'tipo_problema',
            'comentarios_resolucion',
        ]
        widgets = {
            'id_llamada': forms.Select(attrs={'class': 'form-control'}),
            'id_agente_resolvio': forms.Select(attrs={'class': 'form-control'}),
            'descripcion_problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado_problema': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_resolucion_estimada': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'prioridad': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_problema': forms.TextInput(attrs={'class': 'form-control'}),
            'comentarios_resolucion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EncuestaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = EncuestaSatisfaccion
        fields = [
            'id_llamada',
            'fecha_encuesta',
            'calificacion_general',
            'calificacion_agente',
            'comentarios',
            'fecha_envio_encuesta',
            'fue_completada',
        ]
        widgets = {
            'id_llamada': forms.Select(attrs={'class': 'form-control'}),
            'fecha_encuesta': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'calificacion_general': forms.NumberInput(attrs={'class': 'form-control'}),
            'calificacion_agente': forms.NumberInput(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_envio_encuesta': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'fue_completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CampanaForm(forms.ModelForm):
    class Meta:
        model = Campana
        fields = [
            'nombre_campana',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            'tipo_campana',
            'objetivo',
            'publico_objetivo',
            'presupuesto_campana',
        ]
        labels = {
            'nombre_campana': 'Nombre de la Campaña',
            'descripcion': 'Descripción',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Fin',
            'tipo_campana': 'Tipo de Campaña',
            'objetivo': 'Objetivo',
            'publico_objetivo': 'Público Objetivo',
            'presupuesto_campana': 'Presupuesto de la Campaña',
        }
        widgets = {
            'nombre_campana': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tipo_campana': forms.TextInput(attrs={'class': 'form-control'}),
            'objetivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'publico_objetivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'presupuesto_campana': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ParticipacionCampanaForm(forms.ModelForm):
    class Meta:
        model = ParticipacionCampana
        fields = [
            'id_agente',
            'id_campana',
            'fecha_inicio_participacion',
            'fecha_fin_participacion',
            'num_llamadas_realizadas',
            'num_exitos',
            'tiempo_promedio_llamada',
        ]
        labels = {
            'id_agente': 'Agente',
            'id_campana': 'Campaña',
            'fecha_inicio_participacion': 'Fecha de Inicio de Participación',
            'fecha_fin_participacion': 'Fecha de Fin de Participación',
            'num_llamadas_realizadas': 'Llamadas Realizadas',
            'num_exitos': 'Éxitos',
            'tiempo_promedio_llamada': 'Tiempo Promedio por Llamada (segundos)',
        }
        widgets = {
            'id_agente': forms.Select(attrs={'class': 'form-control'}),
            'id_campana': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio_participacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin_participacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'num_llamadas_realizadas': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_exitos': forms.NumberInput(attrs={'class': 'form-control'}),
            'tiempo_promedio_llamada': forms.NumberInput(attrs={'class': 'form-control'}),
        }
