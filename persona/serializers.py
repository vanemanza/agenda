from rest_framework import serializers, pagination
from .models import Person, Reunion, Hobby


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__' # le indico q traiga todos los campos del modelo Person

class PersonaSerializer(serializers.Serializer):

    # espera un queryset q tenga estas caracteristicas:
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

class SerializerDos(serializers.Serializer):

    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    #activo = serializers.BooleanField(default=False) # para indicarle q este atributo no es obligatorio
    activo = serializers.BooleanField(required=False)

class PersonaSerializer2(serializers.ModelSerializer):

    activo = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = '__all__'

class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonSerializer()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',            
            'asunto',
            'persona',
        )

class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = '__all__'

class PersonaHobbySerializer(serializers.ModelSerializer):

    hobbies= HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies'
        )

class ReuSerializerMil(serializers.ModelSerializer):

    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion 
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'
        )        

    def get_fecha_hora(self,obj): #object hace referencia al registro q se está iterando, cada uno de los elem de la lista
        return str(obj.fecha) + '-' + str(obj.hora)    

class PersonaPaginacion(pagination.PageNumberPagination):
    page_size = 5 # los bloques q va mostrando
    max_page_size = 100 #lo q carga en memoria
