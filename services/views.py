from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from services.models import Service, Contact, Sitemap


class ServiceListView(ListView):
    model = Service
    fields = ['id', 'name', 'description', 'price']
    template_name = 'services/service_list.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Все услуги'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = Service.objects.all(*args, **kwargs)
        return queryset


class ServiceCreateView(CreateView):
    model = Service
    fields = '__all__'
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:service_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Создание услуги'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        queryset = Service.objects.all(*args, **kwargs)
        return queryset


class ServiceDetailView(ListView):
    model = Service
    fields = '__all__'
    template_name = 'services/service_detail.html'
    success_url = reverse_lazy('services:service_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подробнее о услуге'
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = Service.objects.filter(id=self.kwargs['pk'])
        return queryset


class ServiceUpdateView(UpdateView):
    model = Service
    fields = '__all__'
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('services:service_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование услуги'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        queryset = Service.objects.all(*args, **kwargs)
        return queryset


class ServiceDeleteView(DeleteView):
    model = Service
    fields = '__all__'
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('services:service_list')


class ContactView(ListView):
    model = Contact
    fields = '__all__'
    template_name = 'services/contact_list.html'


class FeedbackView(ListView):
    model = Contact
    fields = '__all__'
    template_name = 'services/feedback_list.html'


class SitemapView(ListView):
    model = Sitemap
    fields = '__all__'
    template_name = 'services/site_map_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


