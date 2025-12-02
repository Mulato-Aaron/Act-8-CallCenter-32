from django.db import models

class AgenteCallCenter(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    turno = models.CharField(max_length=50, null=True, blank=True)
    habilidades_idiomas = models.TextField(null=True, blank=True)
    estado_agente = models.CharField(max_length=50, null=True, blank=True)
    dni = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_agentes/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ClienteCallCenter(models.Model):
    nombre_empresa = models.CharField(max_length=255, null=True, blank=True)
    contacto_principal = models.CharField(max_length=100, null=True, blank=True)
    email_contacto = models.EmailField(max_length=100, null=True, blank=True)
    telefono_contacto = models.CharField(max_length=20, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    fecha_registro = models.DateField(null=True, blank=True)
    historial_problemas = models.TextField(null=True, blank=True)
    nivel_satisfaccion = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre_empresa

class Llamada(models.Model):
    id_cliente = models.ForeignKey(ClienteCallCenter, on_delete=models.SET_NULL, null=True, blank=True)
    id_agente = models.ForeignKey(AgenteCallCenter, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_hora_inicio = models.DateTimeField(null=True, blank=True)
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)
    duracion_segundos = models.IntegerField(null=True, blank=True)
    tipo_llamada = models.CharField(max_length=50, null=True, blank=True)
    resultado_llamada = models.CharField(max_length=50, null=True, blank=True)
    grabacion_url = models.CharField(max_length=255, null=True, blank=True)
    motivo_llamada = models.TextField(null=True, blank=True)
    calificacion_cliente = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Llamada {self.id} - {self.fecha_hora_inicio}"

class ProblemaReportado(models.Model):
    id_llamada = models.ForeignKey(Llamada, on_delete=models.SET_NULL, null=True, blank=True)
    id_agente_resolvio = models.ForeignKey(AgenteCallCenter, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion_problema = models.TextField(null=True, blank=True)
    estado_problema = models.CharField(max_length=50, null=True, blank=True)
    fecha_resolucion_estimada = models.DateField(null=True, blank=True)
    prioridad = models.CharField(max_length=20, null=True, blank=True)
    tipo_problema = models.CharField(max_length=50, null=True, blank=True)
    comentarios_resolucion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Problema {self.id} - {self.id_llamada}"

class EncuestaSatisfaccion(models.Model):
    id_llamada = models.ForeignKey(Llamada, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_encuesta = models.DateTimeField(null=True, blank=True)
    calificacion_general = models.IntegerField(null=True, blank=True)
    calificacion_agente = models.IntegerField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    fecha_envio_encuesta = models.DateTimeField(null=True, blank=True)
    fue_completada = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"Encuesta de la llamada {self.id_llamada}"

class Campana(models.Model):
    nombre_campana = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    tipo_campana = models.CharField(max_length=50, null=True, blank=True)
    objetivo = models.TextField(null=True, blank=True)
    publico_objetivo = models.TextField(null=True, blank=True)
    presupuesto_campana = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre_campana

class ParticipacionCampana(models.Model):
    id_agente = models.ForeignKey(AgenteCallCenter, on_delete=models.SET_NULL, null=True, blank=True)
    id_campana = models.ForeignKey(Campana, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inicio_participacion = models.DateField(null=True, blank=True)
    fecha_fin_participacion = models.DateField(null=True, blank=True)
    num_llamadas_realizadas = models.IntegerField(null=True, blank=True)
    num_exitos = models.IntegerField(null=True, blank=True)
    tiempo_promedio_llamada = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Participación de {self.id_agente} en {self.id_campana}"
