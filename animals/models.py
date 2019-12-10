from django.db import models
from datetime import datetime, date
import uuid


class AnimalType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256, verbose_name="Отображаемый вид животного")
    code_name = models.CharField(max_length=256, verbose_name="Код в базе данных, латиницей")

    def __str__(self):
       return self.name




class AnimalBreed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256, verbose_name="Пародистый")
    code_name = models.CharField(max_length=256, verbose_name="Код в базе данных, латиницей")

    def __str__(self):
        return self.name
    



class Animal(models.Model):

    nickname = models.CharField(max_length=50, verbose_name="Кличка")
    view = models.ForeignKey(AnimalType, on_delete=models.PROTECT, verbose_name="Вид")
    town = models.CharField(max_length=50, default="Не указан", verbose_name="Город")
    breed = models.ForeignKey(AnimalBreed, on_delete=models.PROTECT, verbose_name="Породистый")
    full_description = models.TextField(default="Нет", verbose_name="Полное описание")
    description = models.CharField(max_length=50, verbose_name="Краткое описание")
    receipt_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, verbose_name="Дата сдачи в приют")
    photo = models.ImageField(upload_to="animal_photos", verbose_name="Фото")
 
    def __str__(self):
        return self.nickname



