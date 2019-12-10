from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q

from .models import Animal, AnimalType, AnimalBreed

#Список всех животных из базы данных
class HomeView(ListView):
    model = Animal
    template_name = 'animals_list.html'
    paginate_by = 12

    def get_queryset(self):
        user_search = self.request.GET.get('search','')
        if user_search:
            return Animal.objects.filter(Q(description__icontains=user_search) | 
                                        Q(town__icontains=user_search) | 
                                        Q(full_description__icontains=user_search))
        else:
            return Animal.objects.all()
    

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animal_detail.html'


class CatList(ListView):
    model = Animal
    cat = AnimalType.objects.get(code_name="CATS")
    queryset = Animal.objects.filter(view=cat)
    template_name = 'animals_list.html'
    paginate_by = 12


class KittyList(ListView):
    model = Animal
    cat = AnimalType.objects.get(code_name="KITTENS")
    queryset = Animal.objects.filter(view=cat)
    template_name = 'animals_list.html'
    paginate_by = 12


class DogList(ListView):
    model = Animal
    dog = AnimalType.objects.get(code_name="DOGS")
    queryset = Animal.objects.filter(view=dog)
    template_name = 'animals_list.html'
    paginate_by = 12


class PuppyList(ListView):
    model = Animal
    dog = AnimalType.objects.get(code_name="PUPPIES")
    queryset = Animal.objects.filter(view=dog)
    template_name = 'animals_list.html'
    paginate_by = 12


class ParrotList(ListView):
    model = Animal
    parrot = AnimalType.objects.get(code_name="PARROTS")
    queryset = Animal.objects.filter(view=parrot)
    template_name = 'animals_list.html'
    paginate_by = 12


class BreedList(ListView):
    model = Animal
    breed = AnimalBreed.objects.get(code_name="YES")
    queryset = Animal.objects.filter(breed=breed)
    template_name = 'animals_list.html'
    paginate_by = 12


class ContactsTemplate(TemplateView):
    template_name = 'contacts.html'