# Generated by Django 3.0 on 2019-12-08 15:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalBreed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Пародистый')),
                ('code_name', models.CharField(max_length=256, verbose_name='Код в базе данных, латиницей')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Отображаемый вид животного')),
                ('code_name', models.CharField(max_length=256, verbose_name='Код в базе данных, латиницей')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='Кличка')),
                ('town', models.CharField(default='Не указан', max_length=50, verbose_name='Город')),
                ('full_description', models.TextField(default='Нет', verbose_name='Полное описание')),
                ('description', models.CharField(max_length=50, verbose_name='Краткое описание')),
                ('receipt_date', models.DateField(blank=True, verbose_name='Дата сдачи в приют')),
                ('photo', models.ImageField(upload_to='animal_photos', verbose_name='Фото')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.AnimalBreed', verbose_name='Породистый')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.AnimalType', verbose_name='Вид')),
            ],
        ),
    ]
