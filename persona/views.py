from django.shortcuts import render
from django.views.generic import ListView 
from .models import Person, Reunion

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    SerializerDos,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaHobbySerializer,
    ReuSerializerMil, 
    PersonaPaginacion
)


class ListaPersonaListView(ListView):
    #model = Person
    template_name = "personas.html" # muestra la info del contexto
    context_object_name = 'personas' # recibe la info del queryset y se la envia al html

    def get_queryset(self): # el queryset hace un llamado a la BD, lista la info y se la pasa al contexto(context_object_name) 
        return Person.objects.all()

class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer    # indica bajo q formato quiero q serialice la información que recibe 
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

class PersonDetailView(RetrieveAPIView): # equivalente al DetailView
    # 1) el detailView necesita q le pasemos un model en donde buscar el registro q necesito
    # el q le paso x la url
    # casi todas las vistas de DRF q necesiten un modelo, usan un QUERYSET en su lugar
    # en el QUERYSET especifico un conjunto de datos donde el RetrieveAPiView va a hacer la busqueda
    # le tengo q pasar un id x parametro para q lo busque en el queryset

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

class PersonasApiLista(ListAPIView):

    serializer_class = PersonaSerializer #trabajando con un serializers.Serializer
    queryset = Person.objects.all()

class Listadiferente(ListAPIView):
    """ lista personas con un campo q no está en el model"""

    serializer_class = SerializerDos
    
    def get_queryset(self):            
        return Person.objects.all()
    

class Listadiferente2(ListAPIView):
    """ lista personas con un campo q no está en el model"""

    serializer_class = PersonaSerializer2
    
    def get_queryset(self):            
        return Person.objects.all()


class ReunionApiList(ListAPIView):

    serializer_class = ReunionSerializer

    def get_queryset(self):
        
        return Reunion.objects.all()

class ReunionCompleta(ListAPIView):
    serializer_class = PersonaHobbySerializer
    queryset = Person.objects.all()


class ReunionApiList22(ListAPIView):

    serializer_class = ReuSerializerMil
    def get_queryset(self):        
        return Reunion.objects.all()

class PersonasPaginadas(ListAPIView): 
    """ vista con paginación"""
    serializer_class = PersonaSerializer 
    pagination_class = PersonaPaginacion
    def get_queryset(self):
        return Person.objects.all()        