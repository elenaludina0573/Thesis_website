from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from doctor.models import Doctor


class DoctorListView(ListView):
    model = Doctor
    fields = ['name', 'patronymic', 'surname', 'specialization', 'qualification']
    template_name = 'doctor/doctor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    success_url = reverse_lazy('doctor: doctor_list')

    def get_queryset(self, *args, **kwargs):
        queryset = Doctor.objects.all(*args, **kwargs)
        return queryset


class DoctorCreateView(CreateView):
    model = Doctor
    fields = ['name', 'patronymic', 'surname','specialization', 'qualification']
    template_name = 'doctor/doctor_form.html'
    success_url = reverse_lazy('doctor:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        queryset =Doctor.object.all(*args, **kwargs)
        return queryset


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor/doctor_detail.html'
    success_url = reverse_lazy('doctor:doctors_list')


class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ['name', 'patronymic', 'surname','specialization', 'qualification']
    template_name = 'doctor/doctor_form.html'
    success_url = reverse_lazy('doctor:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor/doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor:doctor_list')
