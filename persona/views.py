from django.shortcuts import render
from django.views.generic import ListView 
from .models import Person

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .serializers import PersonSerializer


class ListaPersonaListView(ListView):
    #model = Person
    template_name = "personas.html"
    context_object_name = 'personas'

    def get_queryset(self):       
        return Person.objects.all()

class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer    # indica bajo q formato quiero q serialice la información
    # 2) con el serializador convierto el queryset en json y viceversa
    
    # 1) el queryset recupera los datos q quiero convertir en json
    def get_queryset(self):       
        return Person.objects.all()

class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        # filtramos los datos para la busqueda
        kword = self.kwargs['kword'] #self.kworgs trae los argumentos q vienen dentro de la url
        return Person.objects.filter(full_name__icontains=kword)

class PersonCreateView(CreateAPIView):
    # 1) no uso form_class como en CreateView, 
    # el form_class se conecta al modelo en q se tiene q hacer el registro
    # en su lugar uso el serializer_class q tambien puede ser q trabaje con un modelo ( a veces no)
    # 2) no uso template_name, solo el serializador q va a crear el json
    # 3) tampoco uso un success_url xq lo q pase con los nuevos datos registrados es trabajo del front

    serializer_class = PersonSerializer #recibe un json y lo transforma a datos de python

class PersonDetailView(RetrieveAPIView):
    # 1) el detailView necesita q le pasemos un model en donde buscar el registro q necesito
    # el q le paso x la url
    # casi todas las vistas de DRF q necesiten un modelo, usan un QUERYSET en su lugar
    # en el QUERYSET especifico un conjunto de datos donde el RetrieveAPiView va a hacer la busqueda

    serializer_class = PersonSerializer
    # queryset = Person.objects.all() # si lo hago asi va a buscar el pk en todo el modelo
    # queryset = Person.objects.filter(anulate=False) # buscar q hace el anulate-> es una caract del REtrieve?
    queryset = Person.objects.filter() #porque no le indico ningun parametro al filtro? 


class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer # recibe los datos y transforma el resultado y como si fuera el form y el tamplete
    queryset = Person.objects.all()

class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer # recibe los datos y transforma el resultado y como si fuera el form y el tamplete
    queryset = Person.objects.all()








