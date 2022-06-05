from rest_framework import serializers
from .models import Person, Reunion


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__' # le indico q traiga todos los campos del modelo Person

class PersonaSerializer(serializers.Serializer):

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
    #activo = serializers.BooleanField(default=False)
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
            'hora',
            'asunto',
            'persona',
        )