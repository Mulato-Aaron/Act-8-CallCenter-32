from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import (
    AgenteCallCenter, 
    ClienteCallCenter, 
    Llamada, 
    ProblemaReportado,
    EncuestaSatisfaccion,
    Campana,
    ParticipacionCampana
)
from .forms import (
    AgenteForm, 
    ClienteForm, 
    LlamadaForm, 
    ProblemaReportadoForm,
    EncuestaSatisfaccionForm,
    CampanaForm,
    ParticipacionCampanaForm
)

class HomeView(TemplateView):
    template_name = "app_callcenter/home.html"


class AgenteListView(ListView):
    model = AgenteCallCenter
    template_name = "app_callcenter/agente_list.html"
    context_object_name = "object_list"


class AgenteDetailView(DetailView):
    model = AgenteCallCenter
    template_name = "app_callcenter/agente_detail.html"
    context_object_name = "agente"


class AgenteCreateView(CreateView):
    model = AgenteCallCenter
    form_class = AgenteForm
    template_name = "app_callcenter/agente_form.html"
    success_url = reverse_lazy("app_callcenter:agente-list")


class AgenteUpdateView(UpdateView):
    model = AgenteCallCenter
    form_class = AgenteForm
    template_name = "app_callcenter/agente_form.html"
    success_url = reverse_lazy("app_callcenter:agente-list")


class AgenteDeleteView(DeleteView):
    model = AgenteCallCenter
    template_name = "app_callcenter/agente_confirm_delete.html"
    success_url = reverse_lazy("app_callcenter:agente-list")

class ClienteListView(ListView):
    model = ClienteCallCenter
    template_name = "app_callcenter/cliente_list.html"
    context_object_name = "object_list"

class ClienteDetailView(DetailView):
    model = ClienteCallCenter
    template_name = "app_callcenter/cliente_detail.html"
    context_object_name = "cliente"

class ClienteCreateView(CreateView):
    model = ClienteCallCenter
    form_class = ClienteForm
    template_name = "app_callcenter/cliente_form.html"
    success_url = reverse_lazy("app_callcenter:cliente-list")

class ClienteUpdateView(UpdateView):
    model = ClienteCallCenter
    form_class = ClienteForm
    template_name = "app_callcenter/cliente_form.html"
    success_url = reverse_lazy("app_callcenter:cliente-list")

class ClienteDeleteView(DeleteView):
    model = ClienteCallCenter
    template_name = "app_callcenter/cliente_confirm_delete.html"
    success_url = reverse_lazy("app_callcenter:cliente-list")

class LlamadaListView(ListView):
    model = Llamada
    template_name = "app_callcenter/llamada_list.html"
    context_object_name = "object_list"

class LlamadaDetailView(DetailView):
    model = Llamada
    template_name = "app_callcenter/llamada_detail.html"
    context_object_name = "llamada"

class LlamadaCreateView(CreateView):
    model = Llamada
    form_class = LlamadaForm
    template_name = "app_callcenter/llamada_form.html"
    success_url = reverse_lazy("app_callcenter:llamada-list")

class LlamadaUpdateView(UpdateView):
    model = Llamada
    form_class = LlamadaForm
    template_name = "app_callcenter/llamada_form.html"
    success_url = reverse_lazy("app_callcenter:llamada-list")

class LlamadaDeleteView(DeleteView):
    model = Llamada
    template_name = "app_callcenter/llamada_confirm_delete.html"
    success_url = reverse_lazy("app_callcenter:llamada-list")

class ProblemaReportadoListView(ListView):
    model = ProblemaReportado
    template_name = "app_callcenter/problemareportado_list.html"
    context_object_name = "object_list"

class ProblemaReportadoDetailView(DetailView):
    model = ProblemaReportado
    template_name = "app_callcenter/problemareportado_detail.html"
    context_object_name = "problema"

class ProblemaReportadoCreateView(CreateView):
    model = ProblemaReportado
    form_class = ProblemaReportadoForm
    template_name = "app_callcenter/problemareportado_form.html"
    success_url = reverse_lazy("app_callcenter:problema-list")

class ProblemaReportadoUpdateView(UpdateView):
    model = ProblemaReportado
    form_class = ProblemaReportadoForm
    template_name = "app_callcenter/problemareportado_form.html"
    success_url = reverse_lazy("app_callcenter:problema-list")

class ProblemaReportadoDeleteView(DeleteView):
    model = ProblemaReportado
    template_name = "app_callcenter/problemareportado_confirm_delete.html"
    success_url = reverse_lazy("app_callcenter:problema-list")

class EncuestaSatisfaccionListView(ListView):
    model = EncuestaSatisfaccion
    template_name = "app_callcenter/encuestasatisfaccion_list.html"
    context_object_name = "object_list"

class EncuestaSatisfaccionDetailView(DetailView):
    model = EncuestaSatisfaccion
    template_name = "app_callcenter/encuestasatisfaccion_detail.html"
    context_object_name = "encuesta"

class EncuestaSatisfaccionCreateView(CreateView):
    model = EncuestaSatisfaccion
    form_class = EncuestaSatisfaccionForm
    template_name = "app_callcenter/encuestasatisfaccion_form.html"
    success_url = reverse_lazy("app_callcenter:encuesta-list")

class EncuestaSatisfaccionUpdateView(UpdateView):
    model = EncuestaSatisfaccion
    form_class = EncuestaSatisfaccionForm
    template_name = "app_callcenter/encuestasatisfaccion_form.html"
    success_url = reverse_lazy("app_callcenter:encuesta-list")

class EncuestaSatisfaccionDeleteView(DeleteView):
    model = EncuestaSatisfaccion
    template_name = "app_callcenter/encuestasatisfaccion_confirm_delete.html"
    success_url = reverse_lazy("app_callcenter:encuesta-list")

class CampanaListView(ListView):
    model = Campana
    template_name = "app_callcenter/campana_list.html"
    context_object_name = "object_list"

class CampanaDetailView(DetailView):
    model = Campana
    template_name = "app_callcenter/campana_detail.html"
    context_object_name = "campana"

class CampanaCreateView(CreateView):
    model = Campana
    form_class = CampanaForm
    template_name = "app_callcenter/campana_form.html"
    success_url = reverse_lazy("app_callcenter:campana-list")

class CampanaUpdateView(UpdateView):
    model = Campana
    form_class = CampanaForm
    template_name = "app_callcenter/campana_form.html"
    success_url = reverse_lazy("app_callcenter:campana-list")

class CampanaDeleteView(DeleteView):
    model = Campana
    template_name = "app_callcenter/campana_confirm_delete.html"
    success_url = reverse_lazy("app_callcenter:campana-list")


class ParticipacionCampanaListView(ListView):
    model = ParticipacionCampana
    template_name = "app_callcenter/participacioncampana_list.html"
    context_object_name = "object_list"


class ParticipacionCampanaDetailView(DetailView):
    model = ParticipacionCampana
    template_name = "app_callcenter/participacioncampana_detail.html"
    context_object_name = "participacion"


class ParticipacionCampanaCreateView(CreateView):
    model = ParticipacionCampana
    form_class = ParticipacionCampanaForm
    template_name = "app_callcenter/participacioncampana_form.html"
    success_url = reverse_lazy("app_callcenter:participacion-list")


class ParticipacionCampanaUpdateView(UpdateView):
    model = ParticipacionCampana
    form_class = ParticipacionCampanaForm
    template_name = "app_callcenter/participacioncampana_form.html"
    success_url = reverse_lazy("app_callcenter:participacion-list")


class ParticipacionCampanaDeleteView(DeleteView):
    model = ParticipacionCampana
    template_name = "app_callcenter/participacioncampana_confirm_delete.html"
    success_url = reverse_lazy("app_callcenter:participacion-list")
