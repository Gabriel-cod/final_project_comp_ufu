from django.contrib import admin
from django.urls import path

from mission.views import MissionCreateView, MissionListView, MissionUpdateView
from professional.views import (
    OperatorFleetCreateView,
    OperatorFleetListView,
    OperatorFleetUpdateView,
    OperatorProfessionalCreateView,
    OperatorProfessionalListView,
    OperatorProfessionalUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MissionListView.as_view(), name='list_missions'),
    path('criar-missao/', MissionCreateView.as_view(), name='create_mission'),
    path('atualizar-missao/<int:pk>/', MissionUpdateView.as_view(), name='update_mission'),
    path('profissionais/', OperatorProfessionalListView.as_view(), name='list_professionals'),
    path('profissionais/criar/', OperatorProfessionalCreateView.as_view(), name='create_professional'),
    path('profissionais/atualizar/<int:pk>/', OperatorProfessionalUpdateView.as_view(), name='update_professional'),
    path('frotas/', OperatorFleetListView.as_view(), name='list_fleets'),
    path('frotas/criar/', OperatorFleetCreateView.as_view(), name='create_fleet'),
    path('frotas/atualizar/<int:pk>/', OperatorFleetUpdateView.as_view(), name='update_fleet'),
]
