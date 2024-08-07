from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from health.models import Client, Record


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    fields = ['name', 'surname', 'phone', 'address', 'email', 'birth_date', 'created_at']
    template_name = 'health/client_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    success_url = reverse_lazy('health/client_list')

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    fields = '__all__'
    template_name = 'health/client_detail.html'
    success_url = reverse_lazy('health:client_list.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = self.get_object()
        context['title'] = client_item.name
        return context

    def get_queryset(self):
        return Client.objects.filter(id=self.kwargs['pk'])


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    template_name = 'health/client_form.html'
    success_url = reverse_lazy('health:client_list.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание клиента'
        return context

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)

    def get_queryset(self):
        return Client.objects.all()


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'health/client_form.html'
    success_url = reverse_lazy('health:client_list.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = self.get_object()
        context['title'] = client_item.name
        return context

    def get_queryset(self):
        return Client.objects.filter(id=self.kwargs['pk'])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    fields = '__all__'
    template_name = 'health/client_confirm_delete.html'
    success_url = reverse_lazy('health:client_list.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = self.get_object()
        context['title'] = client_item.name
        return context


class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    fields = '__all__'
    template_name = 'health/record_list.html'
    success_url = reverse_lazy('health:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = Client.objects.get(id=self.kwargs['pk'])
        context['title'] = f'Записи клиента {client_item.name} {client_item.surname}'
        return context

    def get_queryset(self):
        return Record.objects.filter(client_id=self.kwargs['pk'])

class RecordCreateView(CreateView):
    model = Record
    fields = '__all__'
    template_name = 'health/record_form.html'
    success_url = reverse_lazy('health:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_item = Client.objects.get(id=self.kwargs['pk'])
        context['title'] = f'Создание записи для клиента {client_item.name} {client_item.surname}'
        return context

    def form_valid(self, form):
        record = form.save(commit=False)
        record.client_id = self.kwargs['pk']
        record.save()
        return super().form_valid(form)

    def get_queryset(self):
        return Record.objects.all()


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    fields = '__all__'
    template_name = 'health/record_detail.html'
    success_url = reverse_lazy('health:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record_item = self.get_object()
        context['title'] = f'Запись клиента {record_item.client.name} {record_item.client.surname}'
        return context

    def get_queryset(self):
        return Record.objects.filter(id=self.kwargs['pk'])


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    fields = '__all__'
    template_name = 'health/record_form.html'
    success_url = reverse_lazy('health:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record_item = self.get_object()
        context['title'] = f'Редактирование записи клиента {record_item.client.name} {record_item.client.surname}'
        return context

    def get_queryset(self):
        return Record.objects.filter(id=self.kwargs['pk'])


class RecordDeleteView(DeleteView):
    model = Record
    fields = '__all__'
    template_name = 'health/record_confirm_delete.html'
    success_url = reverse_lazy('health:record_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record_item = self.get_object()
        context['title'] = f'Удаление записи клиента {record_item.client.name} {record_item.client.surname}'
        return context

