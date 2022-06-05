from django.urls import path 
from .views import (
    ListaPersonaListView, 
    PersonListApiView, 
    PersonSearchApiView, 
    PersonCreateView,
    PersonDetailView,
    PersonDeleteView,
    PersonUpdateView,
    PersonRetriveUpdateView,
)

app_name = 'persona_app'

urlpatterns = [
    path('personas/', ListaPersonaListView.as_view(), name='personas'),
    path('api/persona/list', PersonListApiView.as_view(), name='personas_api'),
    path('api/persona/search/<kword>', PersonSearchApiView.as_view()),
    path('api/persona/create', PersonCreateView.as_view()),
    path('api/persona/detail/<pk>', PersonDetailView.as_view()),
    path('api/persona/delete/<pk>', PersonDeleteView.as_view()),
    path('api/persona/update/<pk>', PersonUpdateView.as_view()),
    path('api/persona/modificar/<pk>', PersonRetriveUpdateView.as_view()),
]