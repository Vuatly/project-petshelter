from django.contrib import admin
from animals.models import AnimalType, Animal, AnimalBreed


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalType)
class AdnimalTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AnimalBreed)
class AnimalBreedAdmin(admin.ModelAdmin):
    pass