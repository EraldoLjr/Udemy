from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recurso'] = Recurso.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

