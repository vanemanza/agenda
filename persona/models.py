#from model_utils.models import TimeStampedModel
from django.db import models

class Hobby(models.Model):
    hobby = models.CharField("Pasatiempo", max_length=50)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"

    def __str__(self):
        return self.hobby    

class Person(models.Model):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField('Nombres', max_length=50)
    job = models.CharField('Trabajo', max_length=30, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField('telefono', max_length=15, blank=True)
    hobbies = models.ManyToManyField(Hobby)


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.full_name

class Reunion(models.Model):
    """ Modelo para reunion """

    persona = models.ForeignKey(Person, on_delete=models.CASCADE)
    fecha = models.DateField()
    asunto = models.CharField("Asunto", max_length=100)

    class Meta:
        verbose_name = "Reunion"
        verbose_name_plural = "Reuniones"

    def __str__(self):
        return self.asunto            