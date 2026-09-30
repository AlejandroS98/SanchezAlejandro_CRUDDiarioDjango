from django.urls import path
from .views import (
    CreateProfile,
    CreateDiario,
    ListDiario,
    DetailDiario,
    UpdateDiario,
    DeleteDiario,
)

urlpatterns = [
    path('crear-perfil/', CreateProfile.as_view(), name='profile_createuser'),

    path('diarios/', ListDiario.as_view(), name='diario_list'),
    path('crear-diario/', CreateDiario.as_view(), name='diario_create'),
    path('diario/<int:pk>/', DetailDiario.as_view(), name='diario_detail'),
    path('diario/<int:pk>/editar/', UpdateDiario.as_view(), name='diario_update'),
    path('diario/<int:pk>/eliminar/', DeleteDiario.as_view(), name='diario_delete'),
]