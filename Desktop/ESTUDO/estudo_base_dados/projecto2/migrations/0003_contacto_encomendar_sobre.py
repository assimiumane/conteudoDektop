# Generated by Django 3.2.4 on 2021-06-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projecto2', '0002_delete_teste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apelido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('contacto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Encomendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apelido', models.CharField(max_length=50)),
                ('dataNascimento', models.DateTimeField()),
                ('telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('morada', models.CharField(max_length=40)),
                ('codigo_postal', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
                ('cor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugestao', models.TextField()),
            ],
        ),
    ]
