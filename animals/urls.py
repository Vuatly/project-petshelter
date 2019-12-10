from django.urls import path

from animals import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts', views.ContactsTemplate.as_view(), name='contacts'),
    path('animal/<int:pk>/', views.AnimalDetailView.as_view(), name="animal"),
    path('cats', views.CatList.as_view(), name='cats_list'),
    path('kittens', views.KittyList.as_view(), name='kittens_list'),
    path('dogs', views.DogList.as_view(), name='dogs_list'),
    path('puppies', views.PuppyList.as_view(), name='puppies_list'),
    path('parrots', views.ParrotList.as_view(), name='parrots_list'),
    path('breed', views.BreedList.as_view(), name='breed_list'),
]
