from django.contrib import admin
from .models import Person, Hobby, Reunion

# Register your models here.
admin.site.register(Person)
admin.site.register(Hobby)
admin.site.register(Reunion)
