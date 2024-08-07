from django.urls import path

from doctor.apps import DoctorConfig
from doctor.views import DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView

app_name = DoctorConfig.name


urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor_form'),
    path('doctor/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_confirm_delete'),
]
